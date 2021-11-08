"""
@Project ：mydjango
@File    ：urls.py
@IDE     ：PyCharm
@Author  ：wangshuo@Crazy
@Date    ：2021/11/6 17:58
"""
from django.urls import path
from sales.views import listorders, listcustomer

# 配置路由
urlpatterns = [
    path('orders/', listorders),
    path('customer/', listcustomer),
]
