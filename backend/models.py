from django.db import models

# Create your models here.

class Course(models.Model):
    dept = models.fields.CharField(max_length=4)
    number = models.fields.IntegerField(max_length=4)
    instructor = models.fields.CharField()
    section = models.fields.IntegerField()
    days = models.fields.CharField()
    startTime = models.fields.TimeField()
    endTime = models.fields.TimeField()
    recitations = models.ManyToManyField("self")
    labs = models.ManyToManyField("self")


