# -*- coding=utf-8 -*-

import redis


class RedisServer():

    def __init__(self):
        self.pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        self.r = redis.Redis(connection_pool=self.pool)

    def get(self, key):
        return self.r.get(key)

    def set(self, key, value):
        self.r.set(key, value)


