from django.shortcuts import render


def home(request):
    return render(request, "myapp/index.html")


def start(request):
    return render(request, "myapp/index.html")
