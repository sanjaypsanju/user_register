from.models import Login,Register
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=("__all__")
        widgets={

        }
class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=("__all__")
        widgets={

        }
