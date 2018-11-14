# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-12 16:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_lineitem_orderitemrelation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('createtime', models.DateTimeField(db_index=True, default=datetime.datetime.now, verbose_name='添加时间')),
                ('flag', models.IntegerField(choices=[(0, '普通会员'), (1, 'VIP会员'), (2, '黄金会员')], default=0, verbose_name='会员控制字段')),
            ],
            options={
                'verbose_name': '会员信息',
                'verbose_name_plural': '会员信息',
                'db_table': 'userprofile',
                'ordering': ['-createtime'],
            },
        ),
        migrations.RemoveField(
            model_name='artsuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='artsuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='购买用户'),
        ),
        migrations.DeleteModel(
            name='ArtsUser',
        ),
    ]
