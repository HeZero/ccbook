# -*- coding=utf-8 -*-

import json
from . import settings
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.db.models import QuerySet
from plugins.translator import translate
from plugins.redis_server import RedisServer


class JsonMiddleWare(MiddlewareMixin):

    redis = RedisServer()

    def ApiResult(self, code, message, data):
        assert code in settings.code.keys()
        data = str(data)
        return json.dumps({'code': code, 'message': message, 'data': data}, ensure_ascii=False)

    def ApiSuccess(self, data):
        return self.ApiResult('100200', 'success', data)

    def process_response(self, request, response):

        lang = request.GET.get("l")
        if not lang:
            lang = settings.LANGUAGE_CODE

        if isinstance(response, str):
            rs = self.ApiSuccess(response)
            return HttpResponse(rs)

        if isinstance(response, QuerySet):
            result = []
            for o in response.all():
                r = {}
                for n, v in vars(o).items():
                    if n == "_state":
                        continue
                    if lang == settings.LANGUAGE_CODE:
                        rv = v
                        orv = self.redis.get(rv)
                        if orv:
                            v = orv
                        else:
                            v = translate(v, "zh-CN", "en")
                            self.redis.set(rv, v)
                        r[n] = v

                    else:
                        r[n] = v
                result.append(r)

            rs = self.ApiSuccess(result)
            return HttpResponse(rs)

        return response