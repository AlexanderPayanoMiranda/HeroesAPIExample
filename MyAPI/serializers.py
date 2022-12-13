from rest_framework import serializers
from MyAPI.models import Hero


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias', )
