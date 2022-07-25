from django.urls import path
from AppPages import views

urlpatterns = [
    path('', views.experiencia, name="Experiencia")
]