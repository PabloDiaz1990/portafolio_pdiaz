from django.urls import path
from AppTemplate import views

urlpatterns = [
    path('', views.inicio, name="Inicio")
]