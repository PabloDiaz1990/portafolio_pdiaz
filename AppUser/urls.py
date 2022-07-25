from django.urls import path
from AppUser import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.usuarios, name="Usuarios"),
    path('login', views.login_user, name="Login"),
    path('signup', views.register_user, name="Registro"),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editarPerfil', views.edit_user, name="EditarPerfil")
]