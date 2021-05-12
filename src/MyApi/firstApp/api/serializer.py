from rest_framework import serializers
from firstApp.models import Parliament1


class Parliament1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Parliament1
        fields = "__all__"
