from rest_framework import serializers
from .models import Agent

class AgentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=64)

    class Meta:
        model = Agent
        fields = ('__all__')