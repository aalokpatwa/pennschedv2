from django.db import models

class Course(models.Model):
    dept = models.fields.CharField(
        max_length=4,
    )
    number = models.fields.IntegerField(
        max_length=4,
    )
    full_code = models.fields.CharField(
        unique=True,
    )


class Section(models.Model):
    # foreign key to course
    section = models.ForeignKey("Course")
    code = models.fields.IntegerField(
        max_length=4,
        null=False,
        blank=False
    )

    # many-to-many to co-requirement sections
    instructor = models.fields.CharField()
    recitations = models.ManyToManyField("self")
    labs = models.ManyToManyField("self")


class Meeting(models.Model):
    section = models.ForeignKey("Section")
    days = models.fields.CharField(
        max_length=7
    )
    start = models.fields.TimeField()
    end = models.fields.TimeField()
