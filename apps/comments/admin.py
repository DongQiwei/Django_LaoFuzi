from django.contrib import admin
import xadmin

from .models import Comment


# Register your models here.
class CommentAdmin(object):
    list_display = ['name', 'title', 'text', 'created_time']  # 添加要显示的列
    search_fields = ['name', 'title', 'text', 'created_time']  # 要查询的列
    list_filter = ['name', 'title', 'text', 'created_time']
    model_icon = 'glyphicon glyphicon-list-alt'


xadmin.site.register(Comment, CommentAdmin)
