from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView

from vacancy.models import Company
from vacancy.serializer import CompanySerializer


class HomePageView(APIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
