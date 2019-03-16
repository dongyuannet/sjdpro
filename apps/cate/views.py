from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.


class CateViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):

    """
    list:
        栏目分类
    retrieve:
        获取单个Id下的所有下级分类
    """
    queryset = Cates.objects.all()
    serializer_class = CatesSerializers

class CateCaseViewsets(viewsets.GenericViewSet,mixins.RetrieveModelMixin):

    """
    retrieve:
        获取单个Id下的所有案例
    """
    queryset = Cates.objects.all()
    serializer_class = CateCaseSerializers


