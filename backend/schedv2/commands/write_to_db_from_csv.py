from django.core.management.base import BaseCommand
import csv
import


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

        # read .csv by row

            # add to DB

            # create holds if any foreign keys not yet created for sections

        # save DB state (if not dry-run)

