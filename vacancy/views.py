from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from vacancy.models import Company, Category, Worker
from vacancy.serializer import CompanySerializer


class HomePageView(APIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        company_count = Company.objects.all().count()
        vacancy_count = Category.objects.all().count()
        worker_count = Worker.objects.all().count()
        return Response({'company_count':company_count,
                         'vacancy_count':vacancy_count,
                         'worker_count':worker_count})
