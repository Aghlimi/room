from django.shortcuts import render,redirect
from Accounts.models import Account
# Create your views here.
def home(request):
    if not request.COOKIES.get("acc"):
        return redirect("/acc/")
    if not Account.objects.filter(username = request.COOKIES.get("acc")).exists():
        return redirect("logout")
    c = str(request.COOKIES.get("acc"))
    return render(request,"home.html",{
        "username":c.split("/")[0],
        "accs":Account.objects.values_list("username",flat=True)
    })