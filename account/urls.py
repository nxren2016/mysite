# encoding:utf-8
from django.conf.urls import url
from .import views
from django.conf import settings

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
]
