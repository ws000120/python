from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from common.models import Customer
import datetime
import json

# 测试案例
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


def listorders(request):
    return HttpResponse('订单22222')


def listcustomer(request):
    # 查询全部
    obj_data = Customer.objects.values()
    # 查看是否按条件查询
    name = request.GET.get('name', None)
    # 过滤
    if name:
        obj_data = obj_data.filter(name=name)
    obj_data = list(obj_data)
    return HttpResponse(json.dumps(obj_data, cls=DateEncoder, ensure_ascii=False))
