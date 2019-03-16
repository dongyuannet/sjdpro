from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .serializers import *
from .models import *
# Create your views here.

class Mp3Viewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    """
    list:
        获取所有mp3资源
    retrieve:
        根据id获取单个mp3资源
    """
    queryset = Music.objects.all()
    serializer_class = Mp3Serializers

class EffectViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    """
    list:
        获取所有特效资源
    retrieve:
        根据id获取单个特效资源
    """
    queryset = Effects.objects.all()
    serializer_class = EffectSerializers

class TitlesViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    """
    list:
        获取所有标题资源
    retrieve:
        根据id获取单个标题资源
    """
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializers

class BrandCateImagesViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    """
    list:
        获取所有一级分类图片资源
    retrieve:
        根据id获取单个图片资源
    """
    queryset = BrandCate.objects.filter(type=1)
    serializer_class = BrandCateSerializers