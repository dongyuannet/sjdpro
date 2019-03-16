from rest_framework import  serializers
from .models import *
from brand.models import BrandCate
class Mp3Serializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('addtime',)

class EffectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Effects
        fields = '__all__'
        read_only_fields = ('addtime',)

class TitlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = '__all__'
        read_only_fields = ('addtime',)

class BrandCateImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = BrandCateImages
        fields = '__all__'
        read_only_fields = ('addtime',)

class BrandCateSerializers(serializers.ModelSerializer):

    re_images = BrandCateImagesSerializers(many=True)
    class Meta:
        model = BrandCate
        fields = '__all__'
        read_only_fields = ('addtime',)