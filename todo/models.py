from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    complete_data = models.DateTimeField(null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class TodoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    todo_number = models.IntegerField()
