from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar
class usuarioformulario(forms.Form):
    Usuario = forms.CharField(max_length=60,required=True)

    Correo_electronico = forms.EmailField(max_length=150,required=True)
    
    Contraseña = forms.CharField(max_length=60,required=True)

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(),required=False
    )

    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('first_name','email','last_name')
    
    def clean_password2(self):
        
        password = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        else:
            return password2
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields=('imagen',)

