from django.contrib import admin
from Task import models


class TaskAmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    list_display_links = ('name',)


admin.site.register(models.Task, TaskAmin)
