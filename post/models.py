from django.db import models
from Accounts.models import Account
# Create your models here.
class Posts(models.Model):
    creater = models.ForeignKey(Account,on_delete=models.CASCADE,blank=1)
    text = models.TextField(blank=1)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="posts")
    count_likes = models.IntegerField(default=0)
    count_comments = models.IntegerField(default=0)
    likers = models.JSONField()
class Comments(models.Model):
    creater = models.ForeignKey(Account,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="comment",blank=1)
    text = models.TextField(blank=1)
    date = models.DateField(auto_now_add=True)
    count_likes = models.IntegerField(default=0)
    count_comments = models.IntegerField(default=0)
    likers = models.JSONField()
class Reacts(models.Model):
    creater = models.ForeignKey(Account,on_delete=models.CASCADE)
    Comment = models.ForeignKey(Comments,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="comment",blank=1)
    text = models.TextField(blank=1)
    date = models.DateField(auto_now_add=True)
    count_likes = models.IntegerField(default=0)
    likers = models.JSONField()