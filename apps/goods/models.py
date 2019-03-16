from django.db import models

# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=20,default='',verbose_name='名称')
    desc = models.CharField(max_length=200,default='',verbose_name='描述')
    pic = models.ImageField(max_length=30,default='',verbose_name='图片',upload_to='goods/')

    class Meta:
        verbose_name = '商品'
        db_table = 'goodsinfo'
        verbose_name_plural = verbose_name
