from django.urls import path
from AppAbout import views

urlpatterns = [
    path('', views.about, name="About")
]