#!/usr/bin/python3
# Copyright 2024 BISITE
# See LICENSE for details.
# Author: BISITE (@bisite on GitHub)


from fastapi import FastAPI
from chatbot_api import config


api = FastAPI(
    version='1.0',
    title = 'chatbot-api',
    description = "Chatbot to act as an assistant while the user is navigating the website.",
    root_path = config.URL_PREFIX,
    debug = config.DEBUG_MODE
)