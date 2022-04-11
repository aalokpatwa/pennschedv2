from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from schedv2.views import ScheduleCreatorViewSet

router = routers.DefaultRouter()
router.register(
    "schedule",
    ScheduleCreatorViewSet,
    "schedule"
)

create_schedule = ScheduleCreatorViewSet.as_view({'post': 'create_schedule'})
list_schedules = ScheduleCreatorViewSet.as_view({'get': 'list'})

urlpatterns = [
    path("schedules/create", create_schedule, name="create schedules"),
    path("schedules/list", list_schedules, name="list schedules"),
    # path('', include(router.urls)),
]
