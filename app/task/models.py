from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .resourses import *


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    place = models.TextField(max_length=255)
    complete = models.BooleanField(default=False, choices=STATUS)
    executor = models.TextField(blank=True, null=True, default='')

    def save(self, *args, **kwargs):
        if self.complete is False:
            super().save(*args, **kwargs)
        else:
            self.time_out = datetime.now()
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tasks', args=[str(self.id)])


# from django.contrib.auth.models import User
# from task.models import *
# Executor.objects.all()

