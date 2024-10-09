from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.urls import path

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

def test(req):
    plantilla = loader.get_template("test.html")
    documento = plantilla.render()
    return HttpResponse(documento)
