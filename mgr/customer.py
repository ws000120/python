"""
@Project ：mydjango
@File    ：customer.py
@IDE     ：PyCharm
@Author  ：wangshuo@Crazy
@Date    ：2021/11/6 23:35
"""
import django.http
from django.http import JsonResponse
import json
from common.models import *


def dispatch(request):
    if request.method == 'GET':
        request.params = request.GET
    # 'POST', 'PUT', 'DELETE' 参数  需要从 request 对象的 body中取出
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 因为取出来都是json格式  需要转换成 对象
        request.params = json.load(request.body)
    action = request.params['action']
    if action == 'listcustmoer':
        return listcustmoer(request)
    elif action == 'addcustmoer':
        return addcustmoer(request)
    elif action == 'modifycustmoer':
        return modifycustmoer(request)
    elif action == 'deletecustmoer':
        return deletecustmoer(request)


def listcustmoer(request):
    result = Customer.objects.values()
    result = list(result)
    return JsonResponse({'ret': 0, 'data': result})


def addcustmoer(request):
    info = request.params['data']
    record = Customer.objects.create(name=info['name'], age=info['age'], phone_number=info['phone_number'],
                                     creation_time=info['creation_time'], qq=info['qq'])
    return JsonResponse({'ret': 0, 'id': record, 'msg': '添加成功'})


def modifycustmoer(request):
    current_id = request.params['id']
    new_data = request.params['newData']
    try:
        custmoer = Customer.objects.get(id=current_id)
    except Customer.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'id为{current_id}的客户不存在'})

    if 'name' in new_data:
        custmoer.name = new_data['name']
    if 'age' in new_data:
        custmoer.age = new_data['age']
    if 'phone_number' in new_data:
        custmoer.phone_number = new_data['phone_number']
    if 'creation_time' in new_data:
        custmoer.creation_time = new_data['creation_time']
    if 'qq' in new_data:
        custmoer.qq = new_data['qq']
    # 注意 一定要save()保存
    custmoer.save()
    return JsonResponse({'ret': 0, 'msg': '修改成功'})


def deletecustmoer(request):
    return JsonResponse({'ret': 0, })
