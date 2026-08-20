from django.shortcuts import render
from rest_framework import viewsets

from .models import Reporter, Issue
from .serializers import ReporterSerializer, IssueSerializer


class ReporterViewSet(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


def home(request):
    return render(request, 'issues/index.html')