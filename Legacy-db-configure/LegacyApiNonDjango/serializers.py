from rest_framework import serializers
from LegacyApiNonDjango.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('actor_id', 'first_name', 'last_name', 'last_update',)
        read_only = ('actor_id',)
