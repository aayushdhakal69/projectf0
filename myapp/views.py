from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact, Member, Allperson
import re
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    # if request.method == "POST":
    #     name = request.POST["name"]
    #     address = request.POST["address"]
    #     phone = request.POST["phone"]
    #     email = request.POST["email"]
    #     content = request.POST["content"]
    #     # print(name, address, phone, email, content)
    #     contact = Contact(
    #         name=name, address=address, phone=phone, email=email, content=content
    #     )
    #     contact.save()
    # return render(request, "contact.html")
    regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    if request.method == "POST":
        name = request.POST["name"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        content = request.POST["content"]
        my_list = [
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            "{",
            "}",
            "\\",
            "_",
            "~",
            "!",
        ]
        g = any(char.isdigit() for char in name)
        if (
            name != ""
            and len(name) > 4
            and regex.search(name) == None
            and name != r"\\"
            and len(name) < 20
            and g != True
        ):
            # print("Pass")regex.search(name) == None and name!=r"\\"
            contact = Contact(
                name=name, address=address, email=email, phone=phone, content=content
            )
            contact.save()
            send_mail(
                "Hello " + name,
                "Hey thank you for connecting with khetalo.com we will message or can call you shortly",
                "therespawner69@gmail.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "Successfully Received")
            return render(request, "contact.html", {"name": name})
        else:
            messages.info(request, "Please fill the form correctly")
            return redirect("contact")
    else:
        return render(request, "contact.html", {})


def services(request):
    return render(request, "services.html")


# Persons Particular and person list Page
def personlist(request):
    allPosts = Allperson.objects.all()
    # print(allPosts)
    context = {"allPosts": allPosts}
    return render(request, "personlist.html", context)


def personone(request, slug):
    post = Allperson.objects.filter(slug=slug).first()
    context = {"post": post}
    return render(request, "personone.html", context)


def persontwo(request):
    return render(request, "persontwo.html")


def personthree(request):
    return render(request, "personthree.html")


# for testing only in developing mode
def test(request):
    return render(request, "donttouch.html")
