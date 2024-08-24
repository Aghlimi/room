from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from .forms import Create, Login
from post.models import Posts
from .models import *


# Create your views here.
def login(request):
    if request.COOKIES.get("acc"):
        return redirect("/")
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            if Account.objects.filter(username=form.data["username"]).exists():
                if (
                    Account.objects.get(username=form.data["username"]).password
                    == form.data["password"]
                ):
                    r = redirect("/")
                    r.set_cookie("acc", form.data["username"])
                    return r
    return render(request, "login.html", {"form": Login()})


def create(request):
    if request.COOKIES.get("acc"):
        return redirect("/")
    if request.method == "POST":
        form = Create(request.POST, request.FILES)
        if form.is_valid():
            if not Account.objects.filter(username=form.data["username"]).exists():
                # edit check inputs
                form.save()
                r = redirect("/")
                # edit creation cookies
                r.set_cookie("acc", form.data["username"])
                return r
    return render(request, "create.html", {"form": Create})


def logout(request):
    r = redirect("/")
    r.delete_cookie("acc")
    return r


def get_data(request, username):
    if Account.objects.filter(username=username).exists():
        acc = Account.objects.get(username=username)
        return JsonResponse(
            {
                "success": True,
                "username": acc.username,
                "image": acc.image.url,
                "name": acc.name,
                "sex": acc.sex,
                "email": acc.email,
                "date": acc.date,
            }
        )
    else:
        return JsonResponse(
            {
                "success": False,
            }
        )


def profile(request, username):
    if not request.COOKIES.get("acc"):
        return redirect("/")
    if not Account.objects.filter(username=username).exists():
        return render(request,"404.html",{
            "msg":f"{username} profile not found"
        })
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return redirect("logout")
    return render(
        request,
        "profile.html",
        {
            "username": username,
            "posts": Posts.objects.filter(
                creater=Account.objects.get(username=username)
            ),
            "me": request.COOKIES.get("acc"),
        },
    )


def get_all_users(request):
    return JsonResponse({"users": Account.objects.values_list("username", flat=True)})
