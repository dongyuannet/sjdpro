from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.


class CaseFavoViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):

    """
    list:
        案例优惠列表
    retrieve:
        获取单个Id下的优惠列表
    """
    queryset = CaseFavo.objects.all()
    serializer_class = CaseFavoSerializers

class CaseSignsViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):

    """
    list:
        案例报名列表
    retrieve:
        获取单个Id下的报名列表
    """
    queryset = CaseSigns.objects.all()
    serializer_class = CaseSignsSerializers

class CaseViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):

    """
    list:
        案例列表
    retrieve:
        获取单个Id下的列表
    """
    queryset = Acts.objects.all()
    serializer_class = CaseSerializers