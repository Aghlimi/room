from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import redirect as to
from django.http import JsonResponse
from .forms import *
from .models import *


def rm(list, num):
    list2 = []
    for i in list:
        if num != i:
            list2.append(i)
    return list2


def post(request):
    if not request.COOKIES.get("acc"):
        return to("/acc/login")
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return redirect("logout")
    try:
        if request.method == "POST":
            form = Post(request.POST, request.FILES)
            Posts.objects.create(
                creater=Account.objects.get(username=str(request.COOKIES.get("acc"))),
                text=form.data["text"],
                image=request.FILES.get("image"),
                likers={"likers": []},
            )
            return to("/")
    except Exception as r:
        print(r)
    return render(request, "post.html", {"form": Post()})


def postpage(request, post_id):
    if not request.COOKIES.get("acc"):
        return to("/acc/login")
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return redirect("logout")
    if not Posts.objects.filter(id=post_id).exists():
        return render(request, "404.html", {"msg": "post not found"})
    try:
        if request.method == "POST":
            form = Comment(request.POST, request.FILES)
            Comments.objects.create(
                creater=Account.objects.get(username=str(request.COOKIES.get("acc"))),
                post=Posts.objects.get(id=post_id),
                text=form.data["text"],
                image=request.FILES.get("image"),
                likers={"likers": []},
            )
            return JsonResponse({})
    except Exception as r:
        print(r)
    return render(
        request,
        "postpage.html",
        {
            "form": Comment(),
            "post": Posts.objects.get(id=post_id),
            "coms": Comments.objects.filter(post=Posts.objects.get(id=post_id)),
            "me": request.COOKIES.get("acc"),
            "m":""
        },
    )


def comment(request, post_id, comment_id):
    if not request.COOKIES.get("acc"):
        return to("/acc/login")
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return redirect("logout")
    if not Comments.objects.filter(id=comment_id).exists():
        return redirect(f"/post/{post_id}")
    try:
        if request.method == "POST":
            form = React(request.POST, request.FILES)
            Reacts.objects.create(
                creater=Account.objects.get(username=str(request.COOKIES.get("acc"))),
                Comment=Comments.objects.get(id=comment_id),
                text=form.data["text"],
                image=request.FILES.get("image"),
                likers={"likers": []},
            )
            return to(f"/post/{post_id}/{comment_id}")
    except Exception as r:
        print(r)
    return render(
        request,
        "comment.html",
        {
            "form": React(),
            "post": Posts.objects.get(id=post_id),
            "com": Comments.objects.get(id=comment_id),
            "coms": Reacts.objects.filter(Comment=Comments.objects.get(id=comment_id)),
            "me": request.COOKIES.get("acc"),
        },
    )


def like(request, type, post_id):
    if not request.COOKIES.get("acc"):
        return to("acc/login")
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return redirect("logout")
    CLASS = 0
    try:
        id = Account.objects.get(username=str(request.COOKIES.get("acc"))).id
        if type == 1:
            CLASS = Posts.objects.get(id=post_id)
        if type == 2:
            CLASS = Comments.objects.get(id=post_id)
        if type == 3:
            CLASS = Reacts.objects.get(id=post_id)
        likers = CLASS.likers["likers"]
        likes = CLASS.count_likes
        if id in likers:
            likes -= 1
            likers = rm(likers, id)
        else:
            likes += 1
            likers.append(id)
        CLASS.likers["likers"] = likers
        CLASS.count_likes = likes
        CLASS.save()
    except Exception as r:
        print(r)
    return JsonResponse({"like": CLASS.count_likes})


def delete(request, type, id):
    if not request.COOKIES.get("acc"):
        return to("acc/login")
    if not Account.objects.filter(username=request.COOKIES.get("acc")).exists():
        return redirect("logout")
    CLASS = 0
    if type == 1:
        CLASS = Posts.objects.get(id=id)
    if type == 2:
        CLASS = Comments.objects.get(id=id)
    if type == 3:
        CLASS = Reacts.objects.get(id=id)
    CLASS.delete()
    return redirect("/")
