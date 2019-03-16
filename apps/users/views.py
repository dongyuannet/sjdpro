from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

# Create your views here.

class UsersViewsets(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    """
    list:
        用户列表
    retrieve:
        获取指定id的用户
    """
    queryset = UserProfile.objects.all()
    serializer_class = UsersSerializers
    def retrieve(self, request,pk=None):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

class UserResetPwdView(APIView):
    """
    用户重置密码
    """
    def post(self,request):
        serializers = UserResetPwdSerializers(data=request.data)

        if serializers.is_valid():
            password = make_password(serializers.validated_data['password'])
            mobile = serializers.validated_data['mobile']
            user = UserProfile.objects.get(mobile=mobile)
            user.password = password
            user.save()
            return Response({'id':user.id},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    """
    用户登录
    """
    def post(self,request):
        serializers = UserLoginSerializers(data=request.data)
        dict = {}
        if serializers.is_valid():
            dict['id'] = serializers.validated_data['id']
            dict['username'] = serializers.validated_data['username']
            user = UserProfile.objects.get(pk=dict['id'])
            payload = jwt_payload_handler(user)
            dict["token"] = jwt_encode_handler(payload)
            return Response(dict,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class CitysViewsets(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin ):
    """
    list:
        省内列表
    retrieve:
        获取指定id的下级城市或县 区列表
    """
    queryset = China.objects.filter(level=1)
    serializer_class = CitysSerializers
    def retrieve(self, request,pk=None):
        queryset = China.objects.filter(parent=pk)
        serializer = CitysSerializers(queryset,many=True)
        return Response(serializer.data)


class BusinessViewsets(mixins.CreateModelMixin,viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin):
    """
    list:
        获取授权登录商家
    create:
        创建商家
    update:
        更新商家
    """
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return BusinessEditSerializers
        return BusinessSerializers

    def get_permissions(self):
        if self.action == "create":
            return []
        return [IsAuthenticated()]

    def get_queryset(self):
        return Business.objects.filter(user=self.request.user)

    def perform_create (self, serializer):
        mobile = serializer.validated_data['mobile']
        password = serializer.validated_data['password']
        res = UserProfile.objects.create(mobile=mobile,password=make_password(password),is_sj=True,is_active=1,username=mobile)
        if res.id:
            serializer.validated_data.pop('password')
            serializer.validated_data.pop('mobile')
            serializer.validated_data.pop('code')
            serializer.validated_data['user'] = res
            serializer.save()



