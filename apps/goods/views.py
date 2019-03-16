from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .serializers import GoodsSerializers
from .models import Goods
# Create your views here.


class GoodsViewSets(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = GoodsSerializers
    queryset = Goods.objects.all()
