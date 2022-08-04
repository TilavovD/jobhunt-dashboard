from django.urls import path

from vacancy.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view())
]
