# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-12 11:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_art_operator'),
        ('users', '0003_emailverifyrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='单价')),
                ('quantity', models.IntegerField(default=0, verbose_name='购买数量')),
                ('createtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('flag', models.IntegerField(choices=[(0, '待下单'), (1, '已下单')], default=0, verbose_name='购买状态')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Art', verbose_name='小说产品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='购买用户')),
            ],
            options={
                'verbose_name': '购物车条目',
                'verbose_name_plural': '购物车条目',
                'db_table': 'line_item',
            },
        ),
        migrations.CreateModel(
            name='OrderItemRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('line_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.LineItem', verbose_name='关联条目')),
                ('product_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ProductOrder', verbose_name='关联订单')),
            ],
            options={
                'verbose_name': '商品条目和订单关联表',
                'verbose_name_plural': '商品条目和订单关联表',
                'db_table': 'order_item_relation',
            },
        ),
    ]
