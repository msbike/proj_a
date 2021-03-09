from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello Pages</h1>')
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse('<h1>Contact</h1>')
