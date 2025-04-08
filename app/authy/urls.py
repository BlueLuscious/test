from django.contrib import admin
from django.urls import path
from authy.views.sign_up_view import SignUpView


urlpatterns = [
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
]
