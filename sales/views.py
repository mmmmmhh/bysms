from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def listorders(request):
    # listorders的参数request是Django中的 HttpQuest对象，包含了请求中的信息。
    return HttpResponse('下面是系统中的所有订单信息。。。')


def listorders1(request):
    return HttpResponse('下面是系统中的所有订单信息111。。。')


def listorders2(request):
    return HttpResponse('下面是系统中的所有订单信息222。。。')


def listorders3(request):
    return HttpResponse('下面是系统中的所有订单信息333。。。')