from django.db import models
from rest_framework import serializers

from vacancy.models import Company, Worker, Vacancy, Category


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    # workers = WorkerSerializer(many=True)
    workers_count = serializers.IntegerField()
    salary_range = serializers.CharField()
    max_price = serializers.IntegerField()
    min_price = serializers.IntegerField()

    # salary_start = serializers.IntegerField()
    class Meta:
        model = Category
        fields = ("title", "workers_count", "salary_range", "max_price", "min_price")
