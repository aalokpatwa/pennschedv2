import os.path

from django.core.management.base import BaseCommand
import csv
from schedv2.models import Course, Section, Meeting
from os import path
from datetime import datetime


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
            nargs='?',
            type=bool,
            action="store_const",
            const=True,
            default=False,
            help="Include flag if the file "
                 "includes headers labeling columns"
        )

        parser.add_argument(
            "--dry-run",
            nargs='?',
            type=bool,
            action="store_const",
            const=True,
            default=False,
            help="Include flag if want a dry run"
        )


    def handle(self, *args, **options):
        # check for .csv
        if path.splitext(options["path"])[-1].lower() != ".csv":
            raise ValueError(f"path should be .csv")

        # read .csv by row
        with open(options["path"], newline='') as csvfile:
            reader = csv.reader(csvfile)
            if options["header"]:
                next(reader)

            courses = dict()
            sections = dict()
            meetings = set()

            for row in reader:
                # Course
                dept = row[0].strip().upper()
                code = row[1].strip()
                full_code = dept + "-" + row[1].strip()
                if full_code not in courses:
                    courses[full_code] = Course(
                        dept=row[0].strip().upper(),
                        number=int(code),
                        full_code=full_code, # Assumes do not need to be stripped
                    )
                course = course.get(full_code)

                # Section
                section_code = row[3].strip()
                full_section_code = full_code + section_code
                instructor = row[2].strip()
                if full_section_code not in sections:
                    sections[full_section_code] = Section()
                section = sections.get(full_section_code)
                section.course = course
                section.code = int(section_code)
                section.instructor = instructor

                # Meeting
                days = row[4].strip().upper()
                time_fmt = "%I:%M %p"
                start = datetime.strptime(row[5].strip(), time_fmt).time()
                end = datetime.strptime(row[6].strip(), time_fmt).time()
                meetings.add(Meeting(
                    section=section,
                    days=days,
                    start=start,
                    end=end
                ))

                # Recitations & Labs
                for recitation in row[7].split():
                    recitation = recitation.strip()
                    if recitation not in sections:
                        sections[recitation] = Section()
                    section.recitations.add(sections[recitation])

                for lab in row[8].split():
                    lab = lab.strip()
                    if lab not in sections:
                        sections[lab] = Section()
                    section.recitations.add(sections[lab])

        # save DB state (if not dry-run)
        if not options['dry-run']:
            Course.objects.bulk_create(
                courses.values()
            )
            Section.objects.bulk_create(
                sections.values()
            )
            Meeting.objects.bulk_create(
                meetings
            )

