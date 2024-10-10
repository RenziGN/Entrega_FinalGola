from django import forms

class usuarioformulario(forms.Form):
    Usuario = forms.CharField(max_length=60)
    Correo_electronico = forms.EmailField(max_length=150)
    Contraseña = forms.CharField(max_length=60)