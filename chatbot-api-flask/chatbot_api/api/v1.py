#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute (@tobeal on GitHub)


from flask_restx import Api


api = Api(version='1.0',
		  title='chatbot-api',
		  description="Chatbot to act as an assistant while the user is navigating the website.")