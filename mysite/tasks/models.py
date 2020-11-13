from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    period = models.IntegerField()
    last_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Record(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    time_taken = models.IntegerField(default=None, null=True)
    time_completed = models.DateTimeField(default=None, null=True)
    points_awarded = models.IntegerField(default=None, null=True)
    num_users = models.IntegerField(default=None, null=True)

    def __str__(self):
        return "%s - record" % (self.task.name if self.task is not None else "None")

class RecordToUser(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s to %s" % (str(self.record), str(self.user))

class UserToPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    preference = models.IntegerField(default=0)

    def __str__(self):
        return "%s feels %d towards %s" % (str(self.user), self.preference, str(self.task))

