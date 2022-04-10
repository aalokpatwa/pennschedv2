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

urlpatterns = [
    path('', include(router.urls)),
]
