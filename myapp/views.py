from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def services(request):
    return render(request, "services.html")


# Persons Particular Page
def personone(request):
    return render(request, "personone.html")


def persontwo(request):
    return render(request, "persontwo.html")


def personthree(request):
    return render(request, "personthree.html")

def personlist(request):
    return render(request, "personlist.html")
