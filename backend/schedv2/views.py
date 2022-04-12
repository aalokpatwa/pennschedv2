from rest_framework import permissions, mixins, viewsets, generics
from rest_framework.response import Response
from schedv2.models import Course, Section, Meeting
from schedv2.serializers import CourseSerializer, SectionSerializer, MeetingSerializer
from algo.main import main, rank_morningtime

class ScheduleCreatorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = SectionSerializer

    def create_schedule(self, request):
        return Response(data=main(self.get_queryset(), rank_morningtime, None), content_type="application/json")

    def get_queryset(self):
        """
        Get queryset from list of `Course` ids.
        :return: Course queryset
        """
        ids = self.request.data
        return Course.objects.filter(id__in=ids)


class CourseViewSet(
    mixins.ListModelMixin
):
    """
    API endpoint for courses
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer