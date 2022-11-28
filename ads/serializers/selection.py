from rest_framework import serializers

from ads.models.selection import Selection
from ads.serializers.ad import AdSerializer


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'
