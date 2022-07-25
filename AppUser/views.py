from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppUser.forms import RegistroUsuarioForm, EditarUsuarioForm
from django.contrib.auth.decorators import login_required

def usuarios(request):
    return render(request, "usuarios.html")

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "index.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request, "index.html", {"mensaje":"Error, formulareo erroneo"})
    
    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})

def register_user(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "index.html", {"mensaje":"Usuario Creado exitosamente"})
    else:
        form = RegistroUsuarioForm()
    
    return render(request, "registro.html", {"form":form})

@login_required
def edit_user(request):
    usuario = request.user

    if request.method == "POST":
        miFormulario = EditarUsuarioForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "index.html")
    else:
        miFormulario = EditarUsuarioForm(initial={'email':usuario.email})

    return render(request, "editar.html", {"miFormulario": miFormulario, "usuario": usuario})