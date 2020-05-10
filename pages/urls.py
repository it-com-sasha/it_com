from django.urls import path

from . import views

urlpatterns = [
    path('', views.PagesView.as_view())
]
