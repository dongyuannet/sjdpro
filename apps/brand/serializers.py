from rest_framework import serializers
from .models import *
import re
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
import time

class CatesSerializers2(serializers.ModelSerializer):

    class Meta:
        model = BrandCate
        fields = '__all__'

class CatesSerializers(serializers.ModelSerializer):

    sub = CatesSerializers2(many=True)
    class Meta:
        model = BrandCate
        fields = '__all__'

class BrandSerializers(serializers.ModelSerializer):
    code = serializers.ImageField(required=True,help_text='二维码图片')
    banner = serializers.ImageField(required=True,help_text='轮播图')
    name = serializers.CharField(required=True,help_text='门店名称')
    address = serializers.CharField(required=True,help_text='地址')
    location_x = serializers.FloatField(required=True,help_text='位置经度')
    location_y = serializers.FloatField(required=True,help_text='位置纬度')
    contact = serializers.CharField(required=True,help_text='联系方式')
    info = serializers.CharField(required=True,help_text='机构介绍')
    user = serializers.PrimaryKeyRelatedField(required=True, queryset=UserProfile.objects.all(),help_text='用户id')
    cate = serializers.PrimaryKeyRelatedField(required=True,help_text='分类id',queryset=BrandCate.objects.all())

    class Meta:
        model = Brand
        fields = '__all__'
        read_only_fields = ('addtime',)