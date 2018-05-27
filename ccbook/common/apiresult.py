# -*- coding=utf-8 -*-
import json
from ccbook import settings
from django.http import HttpResponse


def ApiResult(code, message, data):
    assert code in settings.code.keys()
    data = str(data)
    result = json.dumps({'code': code, 'message': message, 'data': data})
    return HttpResponse(result)


def ApiSuccess(data):
    return ApiResult('100200', 'success', data)