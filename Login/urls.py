from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', home,name="Inicio"),
    path('store/',store,name="store"),
    path('accounts/register',registro,name="registro"),
    path('accounts/login/',loginsito,name="loginsito"),
    path('about/',about,name="about"),
    path('logout/',LogoutView.as_view(template_name="logout.html"),name="Logout"),
    path('ver_usuarios',ver_usuarios,name="verusuarios"),
    path('accounts/edit/',editar_perfil,name="editarperfil"),
    path('accounts/avatar',agregar_avatar,name="AgregarAvatar"),
    path('accounts/Nopage',nopage,name="Nopage"),
    path('pages',pages,name="pages"),  
    path('elimina_usuario/<int:id>',elimina_usuario,name="eliminar_usuario"),    
]
