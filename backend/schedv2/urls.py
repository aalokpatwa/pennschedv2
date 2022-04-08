from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from schedv2.views import CourseViewSet

router = routers.DefaultRouter()
router.register(
    "courses",
    CourseViewSet,
    "courses"
)

urlpatterns = [
    path('', include(router.urls)),
]
