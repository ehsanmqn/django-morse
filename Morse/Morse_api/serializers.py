from rest_framework import serializers

class MorseAPISerializer(serializers.Serializer):
    input = serializers.CharField(required=True)