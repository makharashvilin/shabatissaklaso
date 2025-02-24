from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
