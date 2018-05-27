# -*- coding:utf-8 -*-

from common.apiresult import *
from .models import *


def index(request):
    return ApiSuccess('hello world')


def getNavgation(request):
    navs = Navigation.objects.filter(use=True)
    return navs


def getBook(request):
    books = Book.objects.all()
    return books


def getBookTranslate(request):
    return None