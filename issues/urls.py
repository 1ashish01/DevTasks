from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ReporterViewSet, IssueViewSet


router = DefaultRouter()

router.register('reporters', ReporterViewSet)
router.register('issues', IssueViewSet)


urlpatterns = [
    path('', include(router.urls)),
]