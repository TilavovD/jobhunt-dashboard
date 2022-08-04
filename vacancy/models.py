from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from helpers.models import BaseModel


# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=128)
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Company(BaseModel):
    title = models.CharField(max_length=128)

    # company_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Vacancy(BaseModel):
    title = models.CharField(max_length=128)
    # vacancy_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Worker(BaseModel):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='workers')

    salary_start = models.PositiveIntegerField(default=0)
    salary_end = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
