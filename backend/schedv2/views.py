from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from backend.schedv2.models import Course, Section, Meeting
from backend.schedv2.serializers import CourseSerializer, SectionSerializer, MeetingSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for courses
    """
    queryset = Course.objects.all().order_by('full_code')
    serializer_class = CourseSerializer