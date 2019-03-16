from django.db import models
from datetime import  datetime
# from users.models import UserProfile
# Create your models here.
CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
class Cates(models.Model):
    name = models.CharField(max_length=255,default='',verbose_name='名称',help_text='名称')
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    cate = models.ForeignKey("self",verbose_name='上级id',help_text='上级id',null=True, blank=True,related_name='sub')
    type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    image = models.ImageField(verbose_name='图片',help_text='图片',upload_to="cate/%Y/%m/%d/",null=True, blank=True,)
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    addtime = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '产品栏目'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


