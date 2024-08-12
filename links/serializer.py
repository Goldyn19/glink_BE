from rest_framework import serializers
from .models import Links


class LinksSerializer(serializers.ModelSerializer):
    label = serializers.CharField()

    class Meta:
        model = Links
        fields = [ 'label',  'link']

    def create(self, validated_data):
        label = validated_data.pop('label')
        link = Links.objects.create(label=label, **validated_data)
        return link


