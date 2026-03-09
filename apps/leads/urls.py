from django.http import HttpResponse
from django.urls import path


def leads_placeholder(request):
    return HttpResponse("Leads app OK")


app_name = "leads"

urlpatterns = [
    path("", leads_placeholder, name="index"),
]