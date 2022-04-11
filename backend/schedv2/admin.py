from django.contrib import admin
from schedv2.models import Course, Section, Meeting

# Register your models here.

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Meeting)