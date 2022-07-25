from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('AppTemplate.urls')),
    path('about/', include('AppAbout.urls')),
    path('pages/', include('AppPages.urls')),
    path('accounts/', include('AppUser.urls')),
    path('admin/', admin.site.urls)
]
