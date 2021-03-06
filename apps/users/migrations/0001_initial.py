# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 17:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户姓名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('flag', models.IntegerField(choices=[(0, '普通会员'), (1, 'vip会员'), (2, '黄金会员')], default=0, verbose_name='会员类型')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'arts_user',
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.BigIntegerField(unique=True, verbose_name='订单号')),
                ('pay_type', models.IntegerField(choices=[(0, '货到付款'), (1, '微信支付'), (2, '支付宝支付')], default=0, verbose_name='支付类型')),
                ('address', models.CharField(default='', max_length=200, verbose_name='配送地址')),
                ('phone', models.BigIntegerField(default=0, verbose_name='联系方式')),
                ('order_time', models.DateTimeField(db_index=True, default=datetime.datetime.now, verbose_name='下单时间')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 'product_order',
            },
        ),
    ]
