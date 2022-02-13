from rest_framework import serializers
class HelloSerializer(serializers.Serializer):
    nombres = serializers.CharField(max_length=10)
    