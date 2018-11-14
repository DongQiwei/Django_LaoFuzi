from django.contrib import admin
from django.conf.urls import url, include

from .views import BookDetail,BookSearch

from django.views.generic import TemplateView

urlpatterns = [
    url('detail/(?P<a_id>\d+)/', BookDetail.as_view(), name='detail'),
    url('search/', BookSearch.as_view(), name='search'),
]
