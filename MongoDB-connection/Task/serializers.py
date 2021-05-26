from rest_framework import serializers
from Task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'name', 'description', 'created_at', )
        read_only = ('id',)
