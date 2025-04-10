from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View


class IndexView(LoginRequiredMixin, View):

    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("index.html")
        return HttpResponse(template.render(None, request))
    