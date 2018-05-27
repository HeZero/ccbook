# -*- coding:utf-8 -*-

from common.apiresult import *
from .models import *


def index(request):
    return ApiSuccess('hello world')


def getNavgation(request):
    navs = Navigation.objects.filter(use=True)
    return navs


def getBook(request):
    books = Book.objects.filter(use=True)
    return books


def getClassify(request):
    classifys = Classify.objects.filter(use=True)
    return classifys


def getRecommend(request):
    return None