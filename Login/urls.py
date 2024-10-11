from django.urls import path
from .views import inicio,store,home,registro,about,loginsito,ver_usuarios
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', home,name="Inicio"),
    path('store/',store,name="store"),
    path('accounts/register',registro,name="registro"),
    path('accounts/login/',loginsito,name="loginsito"),
    path('about/',about,name="about"),
    path('logout/',LogoutView.as_view(template_name="logout.html"),name="Logout"),
    path('ver_usuarios',ver_usuarios,name="verusuarios"),

]
