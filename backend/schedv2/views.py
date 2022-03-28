from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework import permissions
from schedv2.models import Course, Section, Meeting
from schedv2.serializers import CourseSerializer, SectionSerializer, MeetingSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for courses
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer