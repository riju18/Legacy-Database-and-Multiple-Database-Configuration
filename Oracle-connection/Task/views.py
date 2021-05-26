from rest_framework import viewsets, mixins
from Task import serializers
from Task.models import Task


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        task_id = self.request.query_params.get('id')
        if task_id:
            return self.queryset.filter(id=task_id)
        return self.queryset
