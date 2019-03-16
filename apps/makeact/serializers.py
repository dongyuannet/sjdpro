from rest_framework import serializers
from .models import *
import re
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
import time

class MakeactSerializers(serializers.ModelSerializer):
    title = serializers.CharField(required=True,help_text='标题')
    music = serializers.IntegerField(required=True,help_text='音乐id')
    effect = serializers.IntegerField(required=True,help_text='特效id')
    image = serializers.ImageField(required=True,help_text='图片')
    start = serializers.DateTimeField(required=True,help_text='开始时间')
    end = serializers.DateTimeField(required=True,help_text='结束时间')
    case = serializers.IntegerField(required=True,help_text='案例id')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    favo = serializers.CharField(allow_null=True, help_text='优惠')
    brands = serializers.CharField(required=True, help_text='门店')
    signs = serializers.CharField(required=True, help_text='签名')
    class Meta:
        model = Activitys
        fields = '__all__'
        read_only_fields = ('addtime',)

