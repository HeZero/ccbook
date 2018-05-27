# -*- coding=utf-8 -*-

import requests


def translate(content, fromLanguage, toLanguage):
    url = "http://translate.google.cn/translate_a/single?" \
          "client=gtx&sl={0}&tl={1}&ie=UTF-8&oe=UTF-8&dt=t&q={2}".format(fromLanguage, toLanguage, content)
    resp = requests.get(url)
    result = resp.text.split(',')[0]
    return result.replace("[[[", "").replace("\"", "")