"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import xadmin
from django.conf.urls import url, include
from users.views import index_view, LoginView, RegisterView, \
    ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView

# from django.views.generic import TemplateView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    url('^$', index_view, name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url('^captcha/', include('captcha.urls')),
    url('^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url('^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url('^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url('^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

]
