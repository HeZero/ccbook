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
    ranks = Rank.objects.filter(rank_type="RECOMMEND").order_by("rank_num")[0:19]
    if not ranks:
        raise Exception("数据库异常,排名为空")
    bookIds = []
    for rank in ranks:
        bookIds.append(rank.book_uuid)
    books = Book.objects.filter(uni_uuid__in=bookIds)
    return books