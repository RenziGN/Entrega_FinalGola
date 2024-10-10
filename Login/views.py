from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.urls import path
from .models import Usuario
from .forms import usuarioformulario

def inicio(req):
    plantilla = loader.get_template("NavBar.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def store(req):
    plantilla = loader.get_template("store.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def home(req):
    plantilla = loader.get_template("home.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def about(req):
    plantilla = loader.get_template("about.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def registro(req):
    if req.method == 'POST':

        mi_formulario = usuarioformulario(req.POST)
    
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            usuario_nuevo = Usuario(None,Usuario=data['Usuario'],Correo_electronico=data['Correo_electronico'],Contraseña=data['Contraseña'])

            usuario_nuevo.save()
            
            return redirect('Inicio')
        
        else:

            return render(req, "registro.html",{})
        
    else:
        mi_formulario = usuarioformulario()
        return render(req, "registro.html",{"mi_formulario":mi_formulario})