from django import forms
from django.contrib.auth.hashers import make_password
from client.models.client_model import ClientModel


class SignUpForm(forms.ModelForm):

    username = forms.CharField(max_length=128, widget=forms.EmailInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    
    class Meta:
        model = ClientModel
        fields = ["username", "password", ]


    def save(self, commit=True):
        user: "ClientModel" = super().save(commit=False)
        password = self.cleaned_data.get("password")

        if password:
            user.password = make_password(password)
        if commit:
            user.save()
        return user
    