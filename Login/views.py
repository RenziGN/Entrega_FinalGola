from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .forms import UserEditForm,AvatarForm
from django.contrib.auth import login, authenticate
from .models import Usuario,Avatar

def inicio(req):
    
    return render(req, "home.html")

def store(req):
    return render(req, "store.html")

def home(req):
    
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "home.html",{'url':avatar.imagen.url})
    except:
        return render(req, "home.html",{})

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

@login_required
def editar_perfil(req):
    usuario = req.user
    if req.method == 'POST':
        mi_formulario = UserEditForm(req.POST,instance=req.user)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data["password1"])
            mi_formulario.save()

            return redirect('Inicio')
        else:
            return render(req, "editarperfil.html", {"mi_formulario": mi_formulario})
    else:
        mi_formulario = UserEditForm()
        return render(req, "editarperfil.html", {"mi_formulario": mi_formulario})
    
def agregar_avatar(req):
    if req.method == 'POST':
        mi_formulario = AvatarForm(req.POST,req.FILES)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data['imagen'])
            avatar.save()

            return redirect('Inicio')
        else:
            return render(req, "agregar_avatar.html", {"mi_formulario": mi_formulario})
    else:
        mi_formulario = AvatarForm()
        return render(req, "agregar_avatar.html", {"mi_formulario": mi_formulario})
    
def lista_usuarios(req, page):

  print('page:', page)

  cant_por_pagina = 3

  if req.GET.get("direction") == 'next':
    page += 1
  elif req.GET.get("direction") == 'previous':
    page -= 1

  inicio = int(page-1)*cant_por_pagina
  final = int(page)*cant_por_pagina

  lista = Usuario.objects.all()[inicio:final]
  print(lista)

  return render(req, "ver_usuarios.html", {"p": lista, "current_page": page})

def nopage(req):
    return render(req, "Nopage.html")