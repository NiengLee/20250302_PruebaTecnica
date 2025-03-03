from rest_framework import serializers


class ElementSerializer(serializers.Serializer):
    nombre      = serializers.CharField(max_length=50)
    peso        = serializers.IntegerField()
    calorias    = serializers.IntegerField()

class FindBestMatchSerializer(serializers.Serializer):
    elements        = ElementSerializer(many=True)
    min_calories    = serializers.IntegerField()
    max_weight      = serializers.IntegerField()
