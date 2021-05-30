from rest_framework import serializers
from LegacyApi.models import TaskTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTask
        fields = ('id', 'name', 'description', 'created_at', )
        read_only = ('id',)
