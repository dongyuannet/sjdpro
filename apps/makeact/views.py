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


class ActivitysViewsets(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin):

    """
    list:
        获取登录用户发布的活动
    create:
        创建发布的活动
    update:
        修改发布的活动
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    def get_queryset(self):
        return Activitys.objects.filter(user=self.request.user)
    serializer_class = MakeactSerializers

    def perform_create(self, serializer):
        brands = serializer.validated_data['brands']
        signs = serializer.validated_data['signs']
        favo = serializer.validated_data['favo']

