from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # path('<id>/edit', views.edit),
    # path('<id>/hapus', views.hapus),
]