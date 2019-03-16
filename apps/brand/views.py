from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.

class BrandCateViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    """
        list:
            栏目分类
        retrieve:
            获取单个Id下的所有下级分类
    """
    queryset = BrandCate.objects.all()
    serializer_class = CatesSerializers


class BrandViewsets(viewsets.GenericViewSet,mixins.UpdateModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin):
    """
        list:
            获取登录授权的店铺
        update:
            修改店铺
        retrieve:
            获取单个Id下的店铺
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = BrandSerializers

    def get_permissions(self):
        if self.action == 'create':
            return []
        return [IsAuthenticated()]
    def get_queryset(self):
        return Brand.objects.filter(user=self.request.user)

