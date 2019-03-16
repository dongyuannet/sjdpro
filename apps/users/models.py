from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from datetime import  datetime
from sjd.settings import QUSTION

class UserProfile(AbstractUser):
    """
    用户列表
    """
    mobile = models.CharField(default='',max_length=11,verbose_name='手机',help_text='手机')
    wename = models.CharField(default='',max_length=20,verbose_name='微信用户昵称',help_text='微信用户昵称')
    weimage = models.CharField(default='',max_length=255,verbose_name='微信用户头像',help_text='微信用户头像')
    weopenid = models.CharField(default='',max_length=50,verbose_name='微信openid',help_text='微信openid')
    district = models.CharField(default='',max_length=20,verbose_name='地区',help_text='地区')
    sex = models.CharField(max_length=10,choices=(('male','男'),('female','女')),default='male',verbose_name='性别',help_text='性别')
    email = models.EmailField(default='',max_length=20,verbose_name='邮箱',help_text='邮箱')
    is_sj = models.BooleanField(default=False,verbose_name='是否商家',help_text='是否商家')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username



class China(models.Model):
    """
    城市
    """
    parent = models.IntegerField( verbose_name='上级id', help_text="上级id", null=True, blank=True)
    name = models.CharField(default="", max_length=30, verbose_name="名称", help_text="名称")
    level = models.IntegerField(default=2,verbose_name='层级',help_text='层级')
    class Meta:
        verbose_name = '中国城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Business(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE,help_text='用户')
    industry = models.CharField(default='1',max_length=20,choices=(),verbose_name='行业',help_text='行业')
    businame = models.CharField(default='', max_length=255, verbose_name='机构名称', help_text='机构名称')
    status = models.BooleanField(default=False,  verbose_name='是否审核', help_text='是否审核')
    part = models.ForeignKey(China,verbose_name='省/市/县或区',help_text='省/市/县或区')
    qustion = models.CharField(verbose_name='问题',choices=QUSTION,max_length=200,default='q0',help_text='问题')
    addtime = models.DateTimeField(verbose_name='添加时间',default=datetime.now,help_text='添加时间')

    class Meta:
        verbose_name = '商家'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.businame
