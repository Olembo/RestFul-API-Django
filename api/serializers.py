from rest_framework import serializers
from .models import customer

class customerserializers(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = "__all__"