from django.shortcuts import render
from .models import Post

def experiencia(request):
    posts = Post.objects.all()
    return render(request, "experiencia.html", {'posts':posts})
