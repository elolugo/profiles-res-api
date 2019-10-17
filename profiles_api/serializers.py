from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """
    Serializes a name field for testing our APIView.
    Converts and validates the inputs to the methods
    of an API
    """
    name = serializers.CharField(max_length=10)
