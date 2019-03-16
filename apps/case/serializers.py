from rest_framework import serializers
from .models import *
import re
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
import time

class CaseFavoSerializers(serializers.ModelSerializer):

    class Meta:
        model = CaseFavo
        fields = '__all__'

class CaseSignsSerializers(serializers.ModelSerializer):

    class Meta:
        model = CaseSigns
        fields = '__all__'


class CaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Acts
        fields = '__all__'