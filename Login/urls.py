from django.urls import path
from Entrega_Final.views import inicio,test

urlpatterns = [
    
    path('', inicio,name="Inicio"),
    # path('accounts/login/', ),
    path('test/', test,name="Test"),
]
