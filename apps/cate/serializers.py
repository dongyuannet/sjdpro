from rest_framework import serializers
from .models import *
from case.models import *
import re
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
import time

class CatesSerializers2(serializers.ModelSerializer):

    class Meta:
        model = Cates
        fields = '__all__'

class CatesSerializers(serializers.ModelSerializer):

    sub = CatesSerializers2(many=True)
    class Meta:
        model = Cates
        fields = '__all__'

class CaseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Acts
        fields = '__all__'

class CateCaseSerializers(serializers.ModelSerializer):
    re_cate = CaseSerializers(many=True)
    class Meta:
        model = Cates
        fields = '__all__'