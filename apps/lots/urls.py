from django.http import HttpResponse
from django.urls import path


def lots_placeholder(request):
    return HttpResponse("Lots app OK")


app_name = "lots"

urlpatterns = [
    path("", lots_placeholder, name="index"),
]