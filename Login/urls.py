from django.urls import path
from .views import inicio,store,home,test,registro

urlpatterns = [
    
    path('', home,name="Inicio"),
    #path('accounts/login/',),
    path('accounts/register',registro,name="registro"),
    #path('accounts/profile/',),
    path('store/',store,name="store"),
    path('home/',home,name="home"),
    path('test/',test,name="home"),

]
