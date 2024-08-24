from django.db import models
from Accounts.models import Account
# Create your models here.
class Room(models.Model):
    number = models.IntegerField(default=0)
    data = models.JSONField()
    user1 = models.ForeignKey(Account,related_name="user1",on_delete=models.CASCADE)
    user2 = models.ForeignKey(Account,related_name="user2",on_delete=models.CASCADE)
    def __str__(self):
        return self.user1.username + " with " + self.user2.username
    
class Space(models.Model):
    data = models.JSONField()