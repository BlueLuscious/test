import logging
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from client.models.client_model import ClientModel

logger = logging.getLogger(__name__)


class LogInView(LoginView):

    def get(self, request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
        template = loader.get_template("registration/login.html")
        return HttpResponse(template.render(None, request))
    

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        messages.success(self.request, "Login Successfully")
        return super().form_valid(form)


    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = ClientModel.objects.filter(username=username).exists()
        if user:
            user = ClientModel.objects.get(username=username)
            checked_password = check_password(password, user.password)
            if not checked_password:
                logger.info(f"Wrong password")
                messages.error(self.request, "The password is wrong")
        else:
            logger.info(f"User doesn't exist")
            messages.error(self.request, "The user is wrong")
        return super().form_invalid(form)
    