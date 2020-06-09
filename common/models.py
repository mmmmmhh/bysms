from django.db import models

# Create your models here.

# 定义一张数据库表
class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phonenumber = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

    # qq 允许没有字符串：null=True；允许为空值：blank=True
    qq = models.CharField(max_length=30, null=True, blank=True)