from rest_framework import serializers
from .models import *
from brand.models import BrandCate
import re
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
import time
from sjd.settings import QUSTION
from django.contrib.auth.hashers import check_password
cate = BrandCate.objects.filter(type=1)
INDUSTY =  tuple([ (a.id,a.name) for a in cate ])

User = get_user_model()
class CitysSerializers(serializers.ModelSerializer):
    class Meta:
        model = China
        fields = '__all__'


class UsersSerializers(serializers.ModelSerializer):
    sex = serializers.ChoiceField(choices=(('male','男'),('female','女')))
    date_joined = serializers.SerializerMethodField()
    def get_date_joined(self,obj):
        res = obj.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        return res
    class Meta:
        model = UserProfile
        fields = ('username','wename','district','sex','email','mobile','is_sj','date_joined')

class UserLoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=True, help_text='用户名', write_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'}, help_text='密码', min_length=2, write_only=True
    )
    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        if not re.match("^1[358]\d{9}$|^147\d{8}$|^176\d{8}$", username):
            raise serializers.ValidationError("手机号码非法")
        res = UserProfile.objects.filter(username=username)
        if not res:
            raise serializers.ValidationError("用户不存在")
        if not check_password(password, res[0].password):
            raise serializers.ValidationError('密码不正确')
        attrs['id'] = res[0].id
        attrs['mobile'] = attrs['username']
        return attrs
    class Meta:
        model = User
        fields = ('username','mobile','password')

class UserResetPwdSerializers(serializers.Serializer):
    mobile = serializers.CharField(required=True,help_text='用户名',write_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'}, help_text='密码', min_length=2, write_only=True
    )
    code = serializers.CharField(
        required=True, help_text='验证码', write_only=True
    )
    def validate_mobile(self,mobile):
        if not re.match("^1[358]\d{9}$|^147\d{8}$|^176\d{8}$", mobile):
            raise serializers.ValidationError("手机号码非法")
        if not UserProfile.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户不存在")
        return mobile
    def validate_code(self,code):
        if code != '2222':
            raise serializers.ValidationError("验证码错误")
        return code
    class Meta:
        model = UserProfile
        fields = ('username','mobile','password')

class BusinessSerializers(serializers.ModelSerializer):
    bduser = serializers.SerializerMethodField()
    password = serializers.CharField(
        style={'input_type': 'password'},help_text='密码',min_length=2,write_only=True
    )
    mobile = serializers.CharField(
        required=True,help_text='手机号',write_only=True
    )
    businame = serializers.CharField(required=True,min_length=5,help_text='机构名称')
    code = serializers.CharField(
        required=True,help_text='验证码',write_only=True
    )
    industry = serializers.ChoiceField(required=True,help_text='行业',choices=INDUSTY)
    qustion = serializers.ChoiceField(required=True,help_text='问题',choices=QUSTION)

    def validate_mobile(self,mobile):
        if not re.match("^1[358]\d{9}$|^147\d{8}$|^176\d{8}$", mobile):
            raise serializers.ValidationError("手机号码非法")
        if UserProfile.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")
        return mobile
    def validate_code(self,code):
        if code != '2222':
            raise serializers.ValidationError("验证码错误")
        return code

    def get_bduser(self,obj):
        res = UserProfile.objects.get(id=obj.user_id)
        return model_to_dict(res)

    class Meta:
        model = Business
        fields = '__all__'
        read_only_fields = ('addtime','user','status')

class BusinessEditSerializers(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
        read_only_fields = ('addtime','user','status')