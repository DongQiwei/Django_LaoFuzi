from django.conf.urls import url

from pay_test import views

urlpatterns = [
    url('callback/', views.notify_callback, name='callback'),
    url('alipay/', views.pay, name='alipay')
]
