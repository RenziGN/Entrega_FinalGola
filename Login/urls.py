from django.urls import path
from Entrega_Final.views import inicio,store,home,test

urlpatterns = [
    
    path('', home,name="Inicio"),
    #path('accounts/login/',),
    #path('accounts/signup/',),
    #path('accounts/profile/',),
    path('store/',store,name="store"),
    path('home/',home,name="home"),
    path('test/',test,name="home"),

]
