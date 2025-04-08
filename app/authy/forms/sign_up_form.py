from django import forms
from client.models.client_model import ClientModel


class SignUpForm(forms.ModelForm):

    username = forms.CharField(max_length=128, widget=forms.EmailInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    
    class Meta:
        model = ClientModel
        fields = ["username", "password", ]
