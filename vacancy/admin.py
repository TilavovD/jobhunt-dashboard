from django.apps import apps
from django.contrib import admin

from vacancy.models import Worker, Vacancy

models = apps.get_models()


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'salary_start', 'salary_end', 'category', )
    list_filter = ('category', 'salary_start', 'salary_end',)
    search_fields = ('title', 'category')
    ordering = ('title',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', )
    list_filter = ('category',)
    search_fields = ('title', 'category')
    ordering = ('title',)


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
# Register your models here.
