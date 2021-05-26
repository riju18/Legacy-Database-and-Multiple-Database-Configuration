from djongo import models
from django.contrib.auth.models import User
from datetime import datetime


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name
