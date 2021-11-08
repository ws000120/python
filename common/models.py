from django.db import models


# Create your models here.
class Customer(models.Model):
    # 名字
    name = models.CharField(max_length=20)
    # 年龄
    age = models.IntegerField(default=18, null=True)
    # 手机号
    phone_number = models.CharField(max_length=11, null=True)
    # 创建时间
    creation_time = models.DateTimeField(null=True, blank=True)
    # qq
    qq = models.CharField(max_length=20, null=True)
