from rest_framework import serializers
from .models import *
class FilesSerializers(serializers.ModelSerializer):
    file = serializers.FileField(required=True,help_text='文件')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # user = serializers.CharField(required=True)

    class Meta:
        model = Files
        fields = '__all__'
        read_only_fields = ('addtime',)