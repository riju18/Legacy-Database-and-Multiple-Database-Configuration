from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# ************************************************
# django doesn't support different db relation
# with foreign key
# ************************************************

class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
    
    class Meta:
        app_label = 'Task'
        ordering = ('-id',)

    def __str__(self):
        return self.name
