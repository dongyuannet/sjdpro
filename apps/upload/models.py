from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.

class Files(models.Model):

    file = models.FileField(upload_to='allfiles/%Y/%m/%d/',null=True, blank=True,verbose_name='文件',help_text='文件')
    user = models.ForeignKey(UserProfile,verbose_name='用户id',help_text='用户id',null=True,blank=True)
    addtime = models.DateTimeField(default=datetime.now,verbose_name="添加时间",help_text='添加时间')
    class Meta:
        verbose_name = '上传文件'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.id