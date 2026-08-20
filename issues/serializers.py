from rest_framework import serializers
from .models import Reporter, Issue


class ReporterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reporter
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'