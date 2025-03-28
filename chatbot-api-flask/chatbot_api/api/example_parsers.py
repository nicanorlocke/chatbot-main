#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute (@tobeal on GitHub)


from flask_restx import reqparse, inputs



example_parser = reqparse.RequestParser()

example_parser.add_argument('floatparam', location='json', type=float, required=False, help='missing floatparam')
example_parser.add_argument('intparam', location='json', type=int, required=True, help='missing intparam')
example_parser.add_argument('strparam', location='json', type=str, required=True, help='missing strparam')
example_parser.add_argument('dtparam', location='json', type=inputs.date_from_iso8601, required=True, help='missing dtparam')
example_parser.add_argument('nestedparam', location='json', type=dict, required=True, help='missing nestedparam')
example_parser.add_argument('listparam', location='json', type=list, required=True, help='missing listparam')


chatbot_parser = reqparse.RequestParser()
chatbot_parser.add_argument('question', location = 'json', type = str, required = True, help = 'Question to chatbot')

chatbot_chat_parser = reqparse.RequestParser()
chatbot_chat_parser.add_argument('question', location = 'args', type = str, required = True, help = 'Question to chatbot')
