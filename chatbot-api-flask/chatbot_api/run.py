#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute (@tobeal on GitHub)

import time
from flask_cors import CORS
from flask import Flask, Blueprint, redirect, request, g

from chatbot_api import config
from chatbot_api.api.v1 import api
from chatbot_api.api import namespaces
from chatbot_api.core import cache, limiter


app = Flask(__name__)

VERSION = (1, 0)
AUTHOR = 'AIR Institute'


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


@app.before_request
def start_timer():
    g.start_time = time.perf_counter()


@app.after_request
def log_request_time(response):
    if hasattr(g, 'start_time'):
        execution_time = time.perf_counter() - g.start_time
        app.logger.info(f"{request.method} {request.path} tardó {execution_time:.4f} segundos en ejecutarse.")
    return response
    

@app.route('/')
def register_redirection():
    """
    Redirects to dcoumentation page.
    """

    return redirect(f'{request.url_root}/{config.URL_PREFIX}', code=302)


def initialize_app(flask_app):
    """
    This function initializes the Flask Application, adds the namespace and registers the blueprint.
    """

    CORS(flask_app)

    v1 = Blueprint('api', __name__, url_prefix=config.URL_PREFIX)
    api.init_app(v1)

    limiter.exempt(v1)
    cache.init_app(flask_app)

    flask_app.register_blueprint(v1)
    flask_app.config.from_object(config)

    for ns in namespaces:
        api.add_namespace(ns)


def main():
    initialize_app(app)
    separator_str = ''.join(map(str, ["=" for i in range(175)]))
    print(separator_str)
    print(f'Debug mode: {config.DEBUG_MODE}')
    print(f'Authors: {get_authors()}')
    print(f'Version: {get_version()}')
    print(f'Base URL: http://localhost:{config.PORT}{config.URL_PREFIX}')
    print(separator_str)
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG_MODE)



if __name__ == '__main__':
    main()