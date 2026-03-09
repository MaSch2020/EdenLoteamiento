from django.http import HttpResponse
from django.urls import path


def projects_placeholder(request):
    return HttpResponse("Projects app OK")


app_name = "projects"

urlpatterns = [
    path("", projects_placeholder, name="index"),
]