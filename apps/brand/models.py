from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.
CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
class BrandCate(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    cate = models.ForeignKey("self",verbose_name='上级id',help_text='上级id',null=True, blank=True,related_name='sub')
    type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    image = models.ImageField(verbose_name='图片',help_text='图片',upload_to="cate/%Y/%m/%d/",null=True, blank=True,)
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    addtime = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '行业分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name



class Brand(models.Model):
    code = models.ImageField(upload_to='uploads/code/%Y/%m/%d/',verbose_name='二维码图片',help_text='二维码图片',null=True, blank=True)
    banner = models.ImageField(upload_to='uploads/banner/%Y/%m/%d/',verbose_name='轮播图',help_text='轮播图',null=True, blank=True)
    name = models.CharField(max_length=255,verbose_name='门店名称',help_text='门店名称',default='')
    address = models.CharField(max_length=255,verbose_name='地址',help_text='地址',default='')
    location_x = models.FloatField(verbose_name='位置经度',help_text='位置经度',default='')
    location_y = models.FloatField(verbose_name='位置纬度',help_text='位置纬度',default='')
    contact = models.CharField(max_length=255,verbose_name='联系方式',help_text='联系方式',default='')
    info = models.TextField(default='',verbose_name='机构介绍',help_text='机构介绍')
    cate = models.ForeignKey(BrandCate,verbose_name='分类id',help_text='分类id',null=True, blank=True,related_name='re_sub')
    user = models.ForeignKey(UserProfile,verbose_name='用户',help_text='用户',null=True, blank=True,related_name='user_sub')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间',help_text='添加时间')
    class Meta:
        verbose_name = '店铺'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name