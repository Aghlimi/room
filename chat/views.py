from django.shortcuts import render
from django.shortcuts import redirect as t
from django.http import JsonResponse as j
from django.http import FileResponse as file
from .models import Room, Space
from Accounts.models import Account
from django.conf import settings
import datetime
from os.path import join


# Create your views here.
def room(request, username):
    if not request.COOKIES.get("acc"):
        return t("/")
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return t("logout")
    if not Account.objects.filter(username=username).exists():
        return t("/")
    if Room.objects.filter(
        user1=Account.objects.get(username=request.COOKIES.get("acc")),
        user2=Account.objects.get(username=username),
    ).exists():
        pass
    elif Room.objects.filter(
        user2=Account.objects.get(username=request.COOKIES.get("acc")),
        user1=Account.objects.get(username=username),
    ).exists():
        pass
    else:
        Room.objects.create(
            user1=Account.objects.get(username=request.COOKIES.get("acc")),
            user2=Account.objects.get(username=username),
            data={"msgs": []},
        )
    return render(request, "room.html", {"username": username})


def files(request, file):
    path = join(settings.MEDIA_ROOT, file)
    return file(open(path, "rb"))


def chat(request):
    if not request.COOKIES.get("acc"):
        return t("/")
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return t("logout")
    list = []
    for i in Room.objects.filter(user1 = Account.objects.get(username=request.COOKIES.get("acc"))):
        list.append(i.user2.username)
    for i in Room.objects.filter(user2 = Account.objects.get(username=request.COOKIES.get("acc"))):
        list.append(i.user2.username)
    return render(request, "chat.html",{
        "list1":list,
        # "list2":list2,
    })
def send(request, username):
    if not request.COOKIES.get("acc"):
        return t("/")
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return t("logout")
    rom = 0
    if Room.objects.filter(
        user1=Account.objects.get(username=request.COOKIES.get("acc")),
        user2=Account.objects.get(username=username),
    ).exists():
        rom = Room.objects.get(
            user1=Account.objects.get(username=request.COOKIES.get("acc")),
            user2=Account.objects.get(username=username),
        )
    elif Room.objects.filter(
        user2=Account.objects.get(username=request.COOKIES.get("acc")),
        user1=Account.objects.get(username=username),
    ).exists():
        rom = Room.objects.get(
            user2=Account.objects.get(username=request.COOKIES.get("acc")),
            user1=Account.objects.get(username=username),
        )
    else:
        return j({})
    rom.data["msgs"].append(
        {
            "name": request.COOKIES.get("acc"),
            "msg": request.GET.get("msg"),
            "date": datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"),
        }
    )
    rom.number += 1
    rom.save()
    return j({"number": rom.number})


def get(request, username):
    if not request.COOKIES.get("acc"):
        return t("/")
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return t("logout")
    rom = 0
    if Room.objects.filter(
        user1=Account.objects.get(username=request.COOKIES.get("acc")),
        user2=Account.objects.get(username=username),
    ).exists():
        rom = Room.objects.get(
            user1=Account.objects.get(username=request.COOKIES.get("acc")),
            user2=Account.objects.get(username=username),
        )
    elif Room.objects.filter(
        user2=Account.objects.get(username=request.COOKIES.get("acc")),
        user1=Account.objects.get(username=username),
    ).exists():
        rom = Room.objects.get(
            user2=Account.objects.get(username=request.COOKIES.get("acc")),
            user1=Account.objects.get(username=username),
        )
    else:
        return j({})
    
    if request.GET.get("get") == "n":
        return j({"number": rom.number})
    elif request.GET.get("get") == "msgs":
        return j(rom.data)
    return j({})
