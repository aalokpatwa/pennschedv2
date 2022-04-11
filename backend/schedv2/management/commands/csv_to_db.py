from django.core.management.base import BaseCommand
import csv
from schedv2.models import Course, Section, Meeting
from os import path
from datetime import datetime
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from collections import defaultdict


class Command(BaseCommand):
    help = """
    Read in a .csv with columns 
    [Dept,Number,Instructor,Section,Days,Start,End,Recitations,Labs]
    into the database
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            nargs='?',
            required=True,
            type=str,
            help="Path to the .csv file (must be .csv)"
        )

        parser.add_argument(
            "--headers",
            action="store_const",
            const=True,
            default=False,
            help="Include flag if the file "
                 "includes headers labeling columns"
        )

    def handle(self, *args, **options):
        # TODO: handle what happens if another section relies on a
        # check for .csv
        if path.splitext(options["path"])[-1].lower() != ".csv":
            raise ValueError(f"path should be .csv")

        # read .csv by row
        with open(options["path"], newline='') as csvfile:
            reader = csv.reader(csvfile)
            if options["headers"]:
                next(reader)

            sections = dict()
            # lab/recitation (values default to empty list)
            recitation_links, lab_links = defaultdict(list), defaultdict(list)

            with transaction.atomic():
                for row in reader:
                    dept = row[0].strip().upper()
                    code = row[1].strip()
                    full_code = dept + "-" + row[1].strip()
                    section_code = row[3].strip()
                    full_section_code = full_code + section_code
                    instructor = row[2].strip()
                    days = row[4].strip().upper()
                    time_fmt = "%I:%M %p"
                    # Check if times are invalid
                    try:
                        start = datetime.strptime(row[5].strip(), time_fmt).time()
                        end = datetime.strptime(row[6].strip(), time_fmt).time()
                    except ValueError:
                        print(f"Skipped adding {full_code} because" +
                              f" a time was invalid (start time: {row[5]}, end time: {row[6]})")
                        continue

                    # Course
                    try:
                        course = Course.objects.get(full_code=full_code)
                    except ObjectDoesNotExist:
                        course = Course.objects.create(
                            dept=row[0].strip().upper(),
                            number=int(code),
                            full_code=full_code,  # Assumes do not need to be stripped
                        )

                    # Section
                    section = Section.objects.create(
                        course=course,
                        code=int(section_code),
                        instructor=instructor,  # Assumes do not need to be stripped
                    )
                    sections[full_section_code] = section

                    # Meeting
                    Meeting.objects.create(
                        section=section,
                        days=days,
                        start=start,
                        end=end
                    )

                    # Recitations & Labs
                    for recitation in row[7].split():
                        recitation = recitation.strip()
                        if recitation not in sections:
                            recitation_links[recitation].append(section)
                        else:
                            section.recitations.add(sections[recitation])

                    for lab in row[8].split():
                        lab = lab.strip()
                        if lab not in sections:
                            lab_links[lab].append(section)
                        else:
                            section.labs.add(sections[lab])

                    # Backlinks (ie links to where this section is a lab/recitation)
                    for backlink in recitation_links[full_section_code]:
                        backlink.recitations.add(section)
                    for backlink in lab_links[full_section_code]:
                        backlink.labs.add(section)
                    del recitation_links[full_section_code]
                    del lab_links[full_section_code]
            if len(lab_links) > 0 or len(recitation_links) > 0:
                # raise ValueError("Some recitation/lab links could not be added because the"
                #                 "recitation/lab section was never created")
                # TODO: FIXME!!!
                print("Some recitation/lab links could not be added because the recitation/lab section was never created")
                print(lab_links.keys(), recitation_links.keys())