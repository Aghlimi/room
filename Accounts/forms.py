from django import forms
from .models import Account
class Login(forms.Form):
    username = forms.CharField(label="username",max_length=50, required=True)
    password = forms.CharField(label="password", max_length=50, required=True,widget=forms.PasswordInput)
class Create(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "username",
            "email",
            "password",
            "date",
            "sex",
            "name",
            "image",
            "email",
        ]
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'}),
            'password':forms.PasswordInput(attrs={
                'type':'password',
                'placeholder':'password',
            })
        }