from django import forms

class usuarioformulario(forms.Form):
    Usuario = forms.CharField(max_length=60,required=True)

    Correo_electronico = forms.EmailField(max_length=150,required=True)
    
    Contraseña = forms.CharField(max_length=60,required=True)