from django.contrib.auth import get_user_model
import xadmin
from xadmin import views
from .models import *
from case.models import *
from cate.models import *
from brand.models import *
from resoucedit.models import *
from makeact.models import *
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "商家管理后台"
    site_footer = "动源网络"


class UserAdmin(object):
    list_display = ['username', 'mobile', "wename",'is_sj','date_joined']
    search_fields = ['username', 'mobile','wename']
    list_filter = ['username', 'mobile','wename', 'date_joined']

class BusinessAdmin(object):
    list_display = ['businame', 'status', "part",'addtime','industry','qustion','user']
    search_fields = ['businame',]
    list_filter = ['user__mobile', 'businame', 'addtime','status']

class CateAdmin(object):
    list_display = ['name', 'cate', "type",'image','addtime']
    search_fields = ['name',]
    list_filter = ['name', 'type','cate__name']
class BrandCateAdmin(object):
    list_display = ['name', 'cate', "type",'image','addtime']
    search_fields = ['name',]
    list_filter = ['name', 'type','cate__name']
class BrandAdmin(object):
    list_display = ['name','user', 'address', "contact",'info','addtime']
    search_fields = ['name',]
    list_filter = ['name', 'address','contact']

class TitlesAdmin(object):
    list_display = ['name','desc','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]

class BrandImagesAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]

class CaseAttrsAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]

class MusicAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]

class EffectsAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]

class ActsAdmin(object):
    list_display = ['title','addtime']
    search_fields = ['title',]
    list_filter = ['title', ]
class CaseFavoAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]
class CaseBrandsAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]
class CaseSignsAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]

class MakeactAdmin(object):
    list_display = ['title','addtime']
    search_fields = ['title',]
    list_filter = ['title', ]

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserAdmin)
xadmin.site.register(Business, BusinessAdmin)
xadmin.site.register(Cates, CateAdmin)
xadmin.site.register(BrandCate, BrandCateAdmin)
xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(Titles, TitlesAdmin)
xadmin.site.register(BrandCateImages, BrandImagesAdmin)
xadmin.site.register(CaseAttrs, CaseAttrsAdmin)
xadmin.site.register(Music, MusicAdmin)
xadmin.site.register(Effects, EffectsAdmin)

xadmin.site.register(Acts, ActsAdmin)
xadmin.site.register(CaseFavo, CaseFavoAdmin)
xadmin.site.register(CaseBrands, CaseBrandsAdmin)
xadmin.site.register(CaseSigns, CaseSignsAdmin)

xadmin.site.register(Activitys, MakeactAdmin)
class ActFavoAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]
xadmin.site.register(ActFavo, ActFavoAdmin)
class ActBrandsAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]
xadmin.site.register(ActBrands, ActBrandsAdmin)
class ActSignsAdmin(object):
    list_display = ['name','addtime']
    search_fields = ['name',]
    list_filter = ['name', ]
xadmin.site.register(ActSigns, ActSignsAdmin)
