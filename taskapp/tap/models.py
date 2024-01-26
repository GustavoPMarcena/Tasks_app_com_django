from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=1000)
    task_description = models.TextField(max_length=1000)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_name
