from django.urls import path
from .views import inicio,store,home,registro,about

urlpatterns = [
    
    path('', home,name="Inicio"),
    path('store/',store,name="store"),
    path('accounts/register',registro,name="registro"),
    #path('accounts/login/',),
    path('about/',about,name="about"),

]
