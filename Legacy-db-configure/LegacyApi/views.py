from rest_framework import viewsets, mixins
from LegacyApi import serializers
from LegacyApi.models import TaskTask


class LegacyTaskViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    serializer_class = serializers.TaskSerializer
    queryset = TaskTask.objects.all()

    def get_queryset(self):
        task_id = self.request.query_params.get('id')
        if task_id:
            return self.queryset.filter(id=task_id)
        return self.queryset
