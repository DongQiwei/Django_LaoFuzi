from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.

# 小说标签
class Tag(models.Model):
    t_id = models.IntegerField(primary_key=True, verbose_name="标签id")
    t_name = models.CharField(max_length=20, verbose_name="文章标签")
    t_info = models.CharField(max_length=50, verbose_name="标签描述", default="小说", null=True)
    t_createtime = models.DateTimeField(default=datetime.now, null=True, db_index=True, verbose_name="创建时间")
    t_flag = models.IntegerField(verbose_name="控制字段", null=True, default=0, choices=((0, "未删除"), (1, "已删除")))

    def __str__(self):
        return self.t_name

    class Meta:
        db_table = "tag"
        verbose_name = "标签"
        verbose_name_plural = verbose_name
        ordering = ["-t_createtime"]


# 小说内容
class Art(models.Model):
    a_id = models.IntegerField(primary_key=True, verbose_name="小说id")
    a_authorname = models.CharField(max_length=20, verbose_name="小说作者")
    a_title = models.CharField(max_length=100, verbose_name="文章标题")
    a_info = models.CharField(max_length=500, verbose_name="文章描述")
    a_content = UEditorField(verbose_name="文章内容", null=True, width=1000, height=600,
                             imagePath="media/arts_ups/ueditor/",
                             filePath="media/arts_ups/ueditor/",
                             blank=True, toolbars="full", default='')
    a_img = models.CharField(null=True, verbose_name="封面", max_length=150)
    a_createtime = models.DateTimeField(default=datetime.now, db_index=True, null=True, verbose_name="添加时间")
    t_id = models.ForeignKey(Tag, verbose_name="关联文章标签", db_column='t_id', default=0)
    a_price = models.IntegerField(default=0, null=True, verbose_name="单价")
    a_flag = models.IntegerField(default=0, null=True, verbose_name="控制字段", choices=((0, "未删除"), (1, "已删除")))

    # operator = models.ForeignKey("auth.User", default=1, null=True, verbose_name="api操作者")

    def __str__(self):
        return self.a_title

    class Meta:
        verbose_name = "小说"
        verbose_name_plural = verbose_name
        db_table = "art"
        ordering = ["-a_createtime"]


# 小说章节
class Chapter(models.Model):
    a_id = models.ForeignKey(Art, verbose_name="小说", db_column='a_id')
    title = models.CharField(max_length=100, verbose_name="章节标题")
    content = models.CharField(verbose_name="章节url", max_length=300)
    add_time = models.DateTimeField(default=datetime.now, null=True, verbose_name="添加时间")

    class Meta:
        db_table = "chapter"
        verbose_name = "小说章节"
        verbose_name_plural = verbose_name
