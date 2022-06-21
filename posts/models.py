from distutils.command.upload import upload
from time import time
from django.db import models
from users.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "task_user", null = True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    time = models.TimeField()

    def __str__(self):
        return self.title