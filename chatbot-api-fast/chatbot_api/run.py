#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute (@tobeal on GitHub)

import uvicorn

from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware
from fastapi.routing import APIRouter

import time
import logging

from chatbot_api import config
from chatbot_api.api.v1 import api
from chatbot_api.api import namespaces
from chatbot_api.core import cache, limiter

VERSION = (1, 0)
AUTHOR = 'AIR Institute'

logging.basicConfig(level=logging.INFO)

def get_version():
    """
    This function returns the API version that is being used.
    """

    return '.'.join(map(str, VERSION))


def get_authors():
    """
    This function returns the API's author name.
    """

    return str(AUTHOR)


__version__ = get_version()
__author__ = get_authors()


@api.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    logging.info(f"{request.method} {request.url.path} tardó {process_time:.4f} segundos en ejecutarse.")
    response.headers["X-Process-Time"] = str(process_time)
    return response


def initialize_app():
    """
    This function initializes the FastAPI Application, adds the namespace and registers the blueprint.
    """
    
    #Initialize CORS
    api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    #Initialize Rate Limiting
    api.state.limiter = limiter
    api.add_middleware(SlowAPIMiddleware)

    #Create Router
    v1_router = APIRouter()
    for ns in namespaces:
        v1_router.include_router(ns, prefix=config.URL_PREFIX)

    api.include_router(v1_router)


def main():
    initialize_app()
    separator_str = ''.join(map(str, ["=" for i in range(175)]))
    print(separator_str)
    print(f'Debug mode: {config.DEBUG_MODE}')
    print(f'Authors: {get_authors()}')
    print(f'Version: {get_version()}')
    print(f'Swagger URL: http://localhost:{config.PORT}{config.URL_PREFIX}/docs')
    print(separator_str)
    uvicorn.run(api, host=config.HOST, port=config.PORT)


if __name__ == '__main__':
    main()