from django.contrib import admin

# Register your models here.
from xadmin import views
import xadmin

from users.models import UserProfile
from books.models import Art, Tag, Chapter
from users.models import UserProfile
from comments.models import Comment


class GlobalSetting(object):
    site_title = '老夫子书城后台管理'  # 设置头标题
    site_footer = '老夫子在线书城'  # 设置脚标题
    menu_style = 'accordion'
    global_search_models = [Tag, Chapter, Art, UserProfile, Comment]


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


class UserAdmin(object):
    list_display = ['username', 'password', 'email', 'is_active']  # 添加要显示的列
    search_fields = ['username', 'password', 'email', 'is_active']  # 要查询的列
    list_filter = ['username', 'password', 'email', 'is_active']
    model_icon = 'glyphicon glyphicon-user'


xadmin.site.register(UserProfile, UserAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
