from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

from users.views import RegisterView, LoginView, ActiveUserView, LogoutView
from message.views import MessageView
from users import views
import xadmin

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('^$', views.index, name='index'),
    url(r'captcha', include('captcha.urls')),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^logout/$', LogoutView.as_view(), name='logout'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url('books/', include('books.urls', namespace='books')),
    url('user/', include('users.urls', namespace='users')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url('^message/$', MessageView.as_view(), name='message'),
    url('pay/', include('pay_test.urls', namespace='pay')),
]
