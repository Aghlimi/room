from django.db import models

# Create your models here.
class Account(models.Model):
    H = [
        ('Male','Male'),
        ('Female','Female')
    ]
    username = models.CharField(max_length=50,blank=0)
    password = models.CharField(max_length=50,blank=0)
    name = models.CharField(max_length=50,blank=0)
    sex = models.CharField(max_length=6,choices=H,blank=0)
    image = models.ImageField(upload_to="profile",default="profile/avatar-default.svg")
    email = models.EmailField(blank=0)
    date = models.DateField(blank=0)
    def __str__(self):
        return self.username
    