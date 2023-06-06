from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        content = request.POST["content"]
        # print(name, address, phone, email, content)
        contact = Contact(
            name=name, address=address, phone=phone, email=email, content=content
        )
        contact.save()
    return render(request, "contact.html")


def services(request):
    return render(request, "services.html")


# Persons Particular and person list Page
def personlist(request):
    return render(request, "personlist.html")


def personone(request):
    return render(request, "personone.html")


def persontwo(request):
    return render(request, "persontwo.html")


def personthree(request):
    return render(request, "personthree.html")


# for testing only in developing mode
def test(request):
    return render(request, "donttouch.html")
