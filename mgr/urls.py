"""
@Project ：mydjango
@File    ：urls.py
@IDE     ：PyCharm
@Author  ：wangshuo@Crazy
@Date    ：2021/11/6 17:58
"""
from django.urls import path
from mgr import customer, sign_in_out

# 配置路由
urlpatterns = [
    path('custmoer/', customer.dispatch),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
]
