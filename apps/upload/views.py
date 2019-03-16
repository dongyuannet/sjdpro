from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.


class UploadViewsets(viewsets.GenericViewSet,mixins.CreateModelMixin):
    """
        create:
            上传文件
    """
    # queryset = Files.objects.all()
    serializer_class = FilesSerializers
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    def get_queryset(self):
        return Files.objects.filter(user=self.request.user)

