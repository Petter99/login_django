from django import forms
from .models import User

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

#class LoginUserForm(forms.ModelForm):
#    class Meta:
#        model  = User
#        fields = ['email', 'password']
#        widgets = {
#            'password': forms.PasswordInput(render_value=True),
#        }
class LoginUserForm(forms.Form):  # No ModelForm
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
