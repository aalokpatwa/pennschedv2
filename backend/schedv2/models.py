from django.db import models

class Course(models.Model):
    dept = models.fields.CharField(
        max_length=4,
        null=False,
        blank=False
    )

    number = models.fields.IntegerField(
        max_length=4,
        null=False,
        blank=False
    )

    full_code = models.fields.CharField(
        max_length=10,
        unique=True,
        null=False,
        blank=False
    )


class Section(models.Model):
    class Meta:
        models.constraints.UniqueConstraint(
            'code',
            'course',
            name="code_course_unique_constraint"
        )

    section = models.ForeignKey(
        "Course",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    code = models.fields.IntegerField(
        max_length=4,
        null=False,
        blank=False,
    )

    instructor = models.fields.CharField(
        null=False
    )

    recitations = models.ManyToManyField("self")
    labs = models.ManyToManyField("self")


class Meeting(models.Model):
    section = models.ForeignKey(
        "Section",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    days = models.fields.CharField(
        max_length=7,
        help_text="String of days MTWRF" # TODO: determine if need sat/sun
    )

    start = models.fields.TimeField(
        null=False,
        blank=False
    )

    end = models.fields.TimeField(
        null=False,
        blank=False
    )

