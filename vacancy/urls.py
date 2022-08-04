from django.urls import path

from vacancy.views import HomePageView, CategoryListView

urlpatterns = [
    path("", HomePageView.as_view()),
    path("category/", CategoryListView.as_view()),

]
