from django.db import models
from django.db.models.lookups import GreaterThan

# Create your views here.
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from vacancy import models as md
from vacancy import serializer


class HomePageView(APIView):
    serializer_class = serializer.CompanySerializer
    queryset = md.Company.objects.all()

    def get(self, request):
        """
        Return a list of all users.
        """
        company_count = md.Company.objects.all().count()
        vacancy_count = md.Vacancy.objects.all().count()
        worker_count = md.Worker.objects.all().count()
        return Response({
            'company_count': company_count,
            'vacancy_count': vacancy_count,
            'worker_count': worker_count
        })


class CategoryListView(APIView):
    serializer_class = serializer.CategorySerializer
    queryset = md.Category.objects.all()

    # @method_decorator(cache_page(60 * 60))
    # def get_queryset(self):
    #     return self.queryset.aggregate(
    #
    #         workers_count=models.Count('workers'),
    #         max_price=models.Max('workers__salary_end'),
    #         min_price=models.Min('workers__salary_start'),
    #         salary_1=(models.F("min_price") + (models.F("min_price") + models.F("max_price")) / 2) / 2,
    #         salary_2=(models.F("max_price") + (models.F("min_price") + models.F("max_price")) / 2 / 2),
    #         salary_avg=(models.F("min_price")+models.F("max_price"))/2,
    #         salary_range=models.Case(
    #             models.When(GreaterThan(models.Max('workers__salary_end'), 2 * models.Min('workers__salary_start')),
    #                         then="salary_start"),
    #
    #             default="salary_avg",
    #             output_field=models.PositiveIntegerField(),
    #         ))
    def get(self, request):
        queryset = md.Category.objects.all()

        qs = queryset.annotate(
            workers_count=models.Count('workers'),
            max_price=models.Max('workers__salary_end'),
            min_price=models.Min('workers__salary_start'), )
        lst = []
        for i in range(len(qs)):
            workers_count = qs[i].workers_count
            max_price = qs[i].max_price
            min_price = qs[i].min_price
            avg_price = (max_price + min_price) / 2
            if max_price > 2 * min_price:
                price = f"{int((min_price + avg_price) / 2)}-{int((avg_price + max_price) / 2)}"
            else:
                price = int(avg_price)
            lst.append({"workers_count": qs[i].workers_count,
                        "max_price": qs[i].max_price,
                        "min_price": min_price,
                        "price": price, }
                       )

            # salary_1=(models.Min('workers__salary_start') + (
            #             models.Min('workers__salary_start') + models.Max('workers__salary_end')) / 2) / 2, )
        # salary_2=(models.F("max_price") + (models.F("min_price") + models.F("max_price")) / 2 / 2),
        # salary_avg=(models.F("min_price")+models.F("max_price"))/2,
        # salary_range=models.Case(
        #     models.When(GreaterThan(models.Max('workers__salary_end'), 2 * models.Min('workers__salary_start')),
        #                 then="salary_start"),
        #
        #     default="salary_avg",
        #     output_field=models.PositiveIntegerField(),
        # ))
        # print(len(self.queryset))

        return Response(lst)
