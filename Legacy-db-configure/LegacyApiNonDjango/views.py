from rest_framework import viewsets, mixins
from LegacyApiNonDjango import serializers
from LegacyApiNonDjango.models import Actor


class LegacyActorViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    serializer_class = serializers.ActorSerializer
    queryset = Actor.objects.using('nondjangopostgre').all()

    def get_queryset(self):
        actor = self.request.query_params.get('id')
        if actor:
            return self.queryset.filter(actor_id=actor)
        return self.queryset
