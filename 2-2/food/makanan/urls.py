from django.urls import path

from . import views

urlpatterns = [
    path('', views.input),
    path('input_ktgori/', views.ktgori),
]