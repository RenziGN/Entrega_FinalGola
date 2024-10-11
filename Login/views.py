from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Usuario

def inicio(req):
    return render(req, "home.html")  # Cambia 'home.html' según sea necesario

def store(req):
    return render(req, "store.html")

def home(req):
    return render(req, "home.html")

def about(req):
    return render(req, "about.html")

def registro(req):
    if req.method == 'POST':
        mi_formulario = UserCreationForm(req.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return redirect('Inicio')
        else:
            return render(req, "registro.html", {"mi_formulario": mi_formulario})
    else:
        mi_formulario = UserCreationForm()
        return render(req, "registro.html", {"mi_formulario": mi_formulario})

def ver_usuarios(req):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios": usuarios}
    return render(req, "ver_usuarios.html", contexto)

def loginsito(req):
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            psw = form.cleaned_data['password']
            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return redirect('Inicio')
            else:
                return redirect('loginsito')
        else:
            return render(req, "loginsito.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(req, "loginsito.html", {"form": form})
