from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

from .cart import CartView, AddCart, CleanCart, CartOrder, CartOrderSubmit

urlpatterns = [
    url('^cart/view/$', CartView),
    url('^cart/add/$', AddCart),
    url('^cart/delete/$', CleanCart),
    url('^cart/order/$', CartOrder),
    url('^cart/order/submit/$', CartOrderSubmit, name='product_order')
]
