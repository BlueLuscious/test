from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from authy.forms.sign_up_form import SignUpForm
from authy.services.sign_up_form_service import SignUpFormService


class SignUpView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("sign-up.html")
        context = dict(
            form=SignUpForm,
        )
        return HttpResponse(template.render(context, request))
    

    def post(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("sign-up.html")
        
        form = SignUpForm(request.POST)
        form_service = SignUpFormService(form)
        validated_data = form_service.validate_form()
        validated_data.save()
        messages.success(request, "Sign up successfully")
        return HttpResponse(template.render(None, request))
