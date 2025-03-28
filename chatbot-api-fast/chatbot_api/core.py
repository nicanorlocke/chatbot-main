#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute (@tobeal on GitHub)

from slowapi import Limiter
from slowapi.util import get_remote_address

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend


limiter = Limiter(
    key_func = get_remote_address,
    default_limits = ["10000 per hour"]
)

cache = FastAPICache.init(
    InMemoryBackend(),
    prefix = "fastapi-cache"
)


cahe_config={
	'CACHE_TYPE': 'simple',
	'CACHE_DEFAULT_TIMEOUT': 1
}