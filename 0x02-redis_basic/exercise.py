#!/usr/bin/env python3
import redis
from uuid import uuid4
from typing import Union

"""Redis exercise"""


class Cache:
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]):
        """Store data in Redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
