from django.db import models
from datetime import  datetime
from resoucedit.models import *
from case.models import *
from django.contrib.auth  import get_user_model
User = get_user_model()

class Activitys(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='标题', help_text='标题')
    music = models.ForeignKey(Music, null=True, blank=True, verbose_name='音乐id', help_text='音乐id')
    effect = models.ForeignKey(Effects, null=True, blank=True, verbose_name='特效id', help_text='特效id')
    image = models.ImageField(upload_to='actimage/%Y/%m/%d/', verbose_name='单张图', help_text='单张图',null=True,blank=True)
    start = models.DateTimeField(verbose_name='开始时间', help_text='开始时间', null=True, blank=True)
    end = models.DateTimeField(verbose_name='结束时间', help_text='结束时间', null=True, blank=True)
    reward_info = models.TextField(default='', verbose_name='奖品说明', help_text='奖品说明')
    act_info = models.TextField(default='', verbose_name='活动说明', help_text='活动说明')
    dui_info = models.TextField(default='', verbose_name='兑奖信息', help_text='兑奖信息')
    intro = models.TextField(default='', verbose_name='机构介绍', help_text='机构介绍')
    attrs = models.ManyToManyField(CaseAttrs, verbose_name='属性列表', help_text='属性列表')
    cate = models.ForeignKey(Cates, verbose_name='分类id', help_text='分类id', null=True, blank=True,related_name='re_cate_act')
    case = models.ForeignKey(Acts, default='', verbose_name='案例id', help_text='案例id',related_name='re_case')
    addtime = models.DateTimeField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')

    user = models.ForeignKey(User,verbose_name='用户id',help_text='用户id',related_name='re_user',null=True,blank=True)
    # favo = models.ManyToManyField(CaseFavo, verbose_name='优惠列表', help_text='优惠列表',default='')
    # brands = models.ManyToManyField(CaseBrands, verbose_name='门店列表', help_text='门店列表')
    # signs = models.ManyToManyField(CaseSigns, verbose_name='报名列表', help_text='报名列表')


    class Meta:
        verbose_name='活动'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

#案例优惠信息
class ActFavo(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    sort = models.IntegerField( verbose_name="排序", help_text="排序",default=1)
    act = models.ForeignKey(Activitys,verbose_name='活动id',help_text='活动id',related_name='re_act')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间',help_text='添加时间')

    class Meta:
        verbose_name = '活动优惠'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

#案例门店信息
class ActBrands(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    location_x = models.FloatField(default='',verbose_name='经度',help_text='经度')
    location_y = models.FloatField(default='',verbose_name='纬度',help_text='纬度')
    address = models.CharField(max_length=255,default='',verbose_name='具体地址',help_text='具体地址')
    phones = models.CharField(max_length=255,default='',verbose_name='手机号组',help_text='手机号组')
    act = models.ForeignKey(Activitys,verbose_name='活动id',help_text='活动id',related_name='re_act_brands')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间',help_text='添加时间')

    class Meta:
        verbose_name = '活动门店'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
#案例报名信息
class ActSigns(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    value = models.CharField(max_length=255,default='',verbose_name='值',help_text='值')
    act = models.ForeignKey(Activitys,verbose_name='活动id',help_text='活动id',null=True, blank=True,related_name='re_act_signs')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间',help_text='添加时间')

    class Meta:
        verbose_name = '活动报名'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name