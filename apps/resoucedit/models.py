from django.db import models
from datetime import  datetime
from brand.models import *
from cate.models import *
# Create your models here.

MUSICTYPE = (
    (1,'热门'),
    (2,'网络歌曲'),
    (3,'节日'),
    (4,'古典'),
    (5,'钢琴'),
    (6,'儿童'),
    (7,'自然')
)

EFFECTSTYPE = (
    (1,'热门'),
    (2,'夏日选集'),
    (3,'促销选集'),
    (4,'图形选集'),
    (5,'自然选集'),
    (6,'节庆选集')
)

class Music(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    mp3 = models.FileField(verbose_name='音乐地址',help_text='音乐地址',upload_to='mp3/%Y/%m/%d/')
    level = models.IntegerField(choices=MUSICTYPE,default=1,verbose_name='类别',help_text='类别')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间',help_text='添加时间')
    class Meta:
        verbose_name = '音乐管理'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Effects(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    level = models.IntegerField(choices=EFFECTSTYPE,default=1,verbose_name='类别',help_text='类别')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间',help_text='添加时间')
    class Meta:
        verbose_name = '特效管理'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
#标题
class Titles(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    desc = models.CharField(default="", verbose_name="描述", help_text="描述",max_length=255)
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间',help_text='添加时间')

    class Meta:
        verbose_name = '标题'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

#一级行业的行业图片
class BrandCateImages(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    image = models.ImageField( verbose_name="描述", help_text="描述",upload_to='brandimage/%Y/%m/%d/')
    cate = models.ForeignKey(BrandCate,verbose_name='分类id',help_text='分类id',null=True, blank=True,related_name='re_images')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间',help_text='添加时间')

    class Meta:
        verbose_name = '品牌分类图片'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

#案例属性
class CaseAttrs(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    value = models.CharField( verbose_name="值", help_text="值",max_length=255,default='')
    cate = models.ForeignKey(Cates,verbose_name='分类id',help_text='分类id',null=True, blank=True,related_name='re_cates')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间',help_text='添加时间')

    class Meta:
        verbose_name = '案例属性'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name



