from django.contrib import admin

# Register your models here.
from books.models import Tag, Art, Chapter
import xadmin


class TagAdmin(object):
    list_display = ['t_id', 't_name', 't_info']  # 添加要显示的列
    search_fields = ['t_id', 't_name', 't_info']  # 要查询的列
    list_filter = ['t_id', 't_name', 't_info']
    model_icon = 'fa fa-cloud'
    list_per_page = 6


class ArtAdmin(object):
    list_display = ['a_id', 'a_authorname', 'a_title', 'a_info']  # 添加要显示的列
    search_fields = ['a_id', 'a_authorname', 'a_title', 'a_info']  # 要查询的列
    list_filter = ['a_id', 'a_authorname', 'a_title', 'a_info']
    style_fields = {'a_content': 'ueditor'}
    model_icon = 'glyphicon glyphicon-book'
    list_per_page = 10


class ChapterAdmin(object):
    list_display = ['title', 'content', 'a_id']  # 添加要显示的列
    search_fields = ['title', 'content', 'a_id']  # 要查询的列
    list_filter = ['title', 'content', 'a_id']
    model_icon = 'glyphicon glyphicon-th-list'
    list_per_page = 50


xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Art, ArtAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
