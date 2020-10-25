from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    points = models.IntegerField(default=0)

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    period = models.IntegerField()
    last_completed = models.DateTimeField(default=None, null=True)

class Record(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    time_taken = models.IntegerField(default=None)
    time_completed = models.DateTimeField(default=None)
    points_awarded = models.IntegerField(default=None)
    num_users = models.IntegerField(default=None)

class RecordToUser(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserToPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    preference = models.IntegerField(default=0)

