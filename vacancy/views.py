from django.db import models
from django.db.models import Count, Sum, Min, Max, Q, F
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from vacancy.models import Company, Category, Worker, Vacancy
from vacancy.serializer import CompanySerializer, CategorySerializer


class HomePageView(APIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        company_count = Company.objects.all().count()
        vacancy_count = Vacancy.objects.all().count()
        worker_count = Worker.objects.all().count()
        return Response({
            'company_count': company_count,
            'vacancy_count': vacancy_count,
            'worker_count': worker_count
        })


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        return self.queryset.annotate(
            workers_count=Count('workers'),
            min_price=Min('workers__salary_start'),
            max_price=Max('workers__salary_end'),
            salary_range=models.Case(
                models.When(Max('workers__salary_end') > 2 * Min('workers__salary_start')),
                then=(
                    f"{(Min('workers__salary_start') + (Min('workers__salary_start') + Max('workers__salary_end')) / 2) / 2}-"
                    f"{((Min('workers__salary_start') + Max('workers__salary_end')) / 2 + Min('workers__salary_start')) / 2}")),
            default=0,
            output_field=models.CharField(),
        ),

        # Min('workers__salary_start') + Sum('workers__salary_end'))
