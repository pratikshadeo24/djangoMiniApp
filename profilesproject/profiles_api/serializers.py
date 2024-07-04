from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serailizes name field for testing API View"""

    name = serializers.CharField(max_length=10)