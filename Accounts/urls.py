from django.urls import path
from .views import login , logout ,create,get_data,profile
urlpatterns = [
    path("",login,name="login"),
    path("create",create,name="create"),
    path("logout",logout,name="logout"),
    path("profile/<str:username>",profile,name="profile"),
    path("get_data/<str:username>",get_data,name="get_data"),
]