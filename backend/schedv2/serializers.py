from rest_framework import serializers
from schedv2.models import Course, Section, Meeting


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'dept', 'number', 'full_code']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'dept', 'number', 'full_code']


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'dept', 'number', 'full_code']
