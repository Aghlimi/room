from django.urls import path
from .views import *
urlpatterns = [
    path("",chat,name="chat"),
    path("<str:username>",room,name="room"),
    path("get/<str:username>",get,name="room"),
    path("send/<str:username>",send,name="room"),
]
