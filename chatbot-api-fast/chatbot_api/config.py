#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute (@tobeal on GitHub)

import os

# api config
PORT = 5001
HOST = '0.0.0.0'
URL_PREFIX = '/chatbot-api/v1'
DEBUG_MODE = True


LANGUAGES = {'es', 'en'}
DEFAULT_LANGUAGE = 'es'
CONTEXT_FILE = 'chatbot_api/model/data/contexts.json'