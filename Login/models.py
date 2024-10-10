from django.db import models

# Create your models here.
class Usuario(models.Model):
    Usuario = models.CharField(max_length=50)
    Correo_electronico = models.EmailField(max_length=150)
    Contraseña = models.CharField(max_length=50)

    def __str__(self):

        return f'{self.Usuario} {self.Correo_electronico} {self.Contraseña}'

class Producto(models.Model):
    Nombre_producto = models.CharField(max_length=100)
    Stock_disponible = models.CharField(max_length=50)

    def __str__(self):

        return f'{self.Nombre_producto} {self.Stock_disponible}'
