from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "id":"username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "id":"user-password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        
        qs = User.objects.filter(username__iexact=username)

        if not qs.exists():
            raise forms.ValidationError("This is an invalid username!")

        return username
