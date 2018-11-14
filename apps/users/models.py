from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

from books.models import Art


# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(max_length=50, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    email = models.EmailField(verbose_name="邮箱")
    is_active = models.IntegerField(default=0, verbose_name="是否激活")
    createtime = models.DateTimeField(default=datetime.now, db_index=True, verbose_name="添加时间")
    flag = models.IntegerField(default=0, verbose_name="会员控制字段", choices=((0, "普通会员"), (1, "VIP会员"), (2, "黄金会员")))

    def __str__(self):
        return self.username

    class Meta:
        db_table = "userprofile"
        verbose_name = "会员信息"
        verbose_name_plural = verbose_name
        ordering = ["-createtime"]


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(verbose_name=u"验证类型", choices=(('register', u'注册'), ('forget', u'找回密码')),
                                 max_length=10)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name


class ProductOrder(models.Model):
    order_id = models.BigIntegerField(verbose_name="订单号", unique=True)
    pay_type = models.IntegerField(verbose_name="支付类型", default=0,
                                   choices=((0, "货到付款"), (1, "微信支付"), (2, "支付宝支付")))
    address = models.CharField(verbose_name="配送地址", max_length=200, default="")
    phone = models.BigIntegerField(verbose_name="联系方式", default=0)
    order_time = models.DateTimeField(verbose_name="下单时间", default=datetime.now, db_index=True)

    def __str__(self):
        return self.order_id

    class Meta:
        db_table = "product_order"
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name


'''
购物车条目
'''


class LineItem(models.Model):
    product = models.ForeignKey(Art, verbose_name="小说产品")
    user = models.ForeignKey(UserProfile, verbose_name="购买用户")
    unit_price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name="单价")
    quantity = models.IntegerField(default=0, verbose_name="购买数量")
    createtime = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    flag = models.IntegerField(default=0, verbose_name="购买状态", choices=((0, "待下单"), (1, '已下单')))

    def __str__(self):
        return self.product.a_title

    class Meta:
        db_table = "line_item"
        verbose_name = "购物车条目"
        verbose_name_plural = verbose_name


'''
商品条目和订单关联表
1   1
3   1
4   1
'''


class OrderItemRelation(models.Model):
    line_item = models.ForeignKey(LineItem, verbose_name="关联条目")
    product_order = models.ForeignKey(ProductOrder, verbose_name="关联订单")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        db_table = "order_item_relation"
        verbose_name = "商品条目和订单关联表"
        verbose_name_plural = verbose_name


'''
购物车
购物车是这些条目的容器。
购物车并不需要记录到数据库中，就好像超市并不关注顾客使用了哪些购物车而只关注他买了什么商品一样。
所以购物车不应该继承自models.Model，而仅仅应该是一个普通类
'''
import time, random


class Cart(object):

    @classmethod
    def add_product(Cls, product, user):
        the_item_products = LineItem.objects.filter(user=user.id, product=product.a_id)
        product_quality_dict = {}
        if len(the_item_products) > 0:
            the_product = the_item_products[0]
            this_quality = the_product.quantity + 1
            # print(f'quality:{this_quality}')
            the_item_products.update(quantity=this_quality)
        else:
            # order_id = "%s%s" % (int(time.time()), random.randint(10, 100))
            # product_order = ProductOrder(order_id=int(order_id))
            # product_order.save()
            l_item = LineItem(product=product,
                              user=user,
                              unit_price=product.a_price,
                              # product_order_id = int(order_id),
                              quantity=1)
            l_item.save()

        return True

    @classmethod
    def get_products(Cls, user):
        product_list = LineItem.objects.filter(user=user.id)

        total_price = 0
        for prod_item in product_list:
            total_price += prod_item.product.a_price * prod_item.quantity
        return (total_price, product_list)
