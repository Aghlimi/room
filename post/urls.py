from django.urls import path
from .views import *
urlpatterns = [
    path("post/",post,name="post"),
    path("like/<int:type>/<int:post_id>",like,name="like"),
    path("post/<int:post_id>/",postpage,name="postpage"),
    path("delete/<int:type>/<int:id>",delete,name="delete"),
    path("post/<int:post_id>/<int:comment_id>",comment,name="comment"),
]
