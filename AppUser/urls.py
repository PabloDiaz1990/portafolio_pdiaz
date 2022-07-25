from django.urls import path
from AppUser import views

urlpatterns = [
    path('', views.usuarios, name="Usuarios")
]