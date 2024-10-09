from django.urls import path
from Entrega_Final.views import inicio,test,test2

urlpatterns = [
    
    path('', inicio,name="Inicio"),
    # path('accounts/login/', ),
    path('test/', test,name="Test"),
    path('test2/', test2,name="Test2"),
]
