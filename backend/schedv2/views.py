from django.shortcuts import render
from rest_framework import permissions, mixins, viewsets, generics
from rest_framework.decorators import api_view
from schedv2.models import Course, Section, Meeting
from schedv2.serializers import CourseSerializer, SectionSerializer, MeetingSerializer

class ScheduleCreatorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
    API endpoint for courses
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @api_view(['POST'])
    def create_schedule(self):
        pass