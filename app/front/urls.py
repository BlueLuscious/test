from django.urls import path
from front.views.index_view import IndexView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
