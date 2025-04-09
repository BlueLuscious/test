from django.urls import path
from authy.views.log_in_view import LogInView
from authy.views.sign_up_view import SignUpView


urlpatterns = [
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("login/", LogInView.as_view(), name="login"),
]
