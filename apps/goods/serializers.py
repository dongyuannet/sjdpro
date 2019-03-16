from .models import Goods
from rest_framework import serializers

class GoodsSerializers(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    desc = serializers.CharField(required=True)
    pic = serializers.ImageField(required=True)

    class Meta:
        model = Goods
        fields = '__all__'

