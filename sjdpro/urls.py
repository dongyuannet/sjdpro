"""sjd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import  obtain_jwt_token
from rest_framework.routers import DefaultRouter
from goods.views import GoodsViewSets
from users.views import *
from cate.views import *
from case.views import *
from brand.views import *
from upload.views import *
from resoucedit.views import *
from makeact.views import *
from django.views.static import serve
from sjd.settings import MEDIA_ROOT
import xadmin

router = DefaultRouter()
# 城市
router.register(r'citys', CitysViewsets, base_name="citys")
# 产品
router.register(r'cate', CateViewsets, base_name="cate")
# 商户申请
router.register(r'business', BusinessViewsets, base_name="business")
# 门店
router.register(r'brandcate', BrandCateViewsets, base_name="brandcate")
router.register(r'brand', BrandViewsets, base_name="brand")

# 上传文件 图片 视频
router.register(r'upload', UploadViewsets, base_name="upload")
# 资源的mp3列表
router.register(r'mp3', Mp3Viewsets, base_name="mp3")
# 特效列表
router.register(r'effect', EffectViewsets, base_name="effect")
# 标题列表
router.register(r'titles', TitlesViewsets, base_name="titles")
# 分类图片
router.register(r'cateimages', BrandCateImagesViewsets, base_name="cateimages")

#优惠信息
router.register(r'casefavo', CaseFavoViewsets, base_name="casefavo")
#报名信息
router.register(r'casesigns', CaseSignsViewsets, base_name="casesigns")
#活动
router.register(r'act', ActivitysViewsets, base_name="act")
#案例
router.register(r'case', CaseViewsets, base_name="case")
#获取指定栏目下的案例
router.register(r'catecase', CateCaseViewsets, base_name="catecase")


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'docs/',include_docs_urls(title='动源网络')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^',include(router.urls)),
    url(r'^token/',obtain_jwt_token),
    url(r'^resetpwd/',UserResetPwdView.as_view(),name='resetpwd'),
    url(r'^login/',UserLoginView.as_view(),name='login'),

    # url(r'^upload/',UploadView.as_view(),name='upload')
]
