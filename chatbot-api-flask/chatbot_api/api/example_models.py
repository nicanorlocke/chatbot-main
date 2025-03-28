#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute @tobeal on GitHub)


from flask_restx import fields

from chatbot_api.api.v1 import api



example_nested_model = api.model('ExampleNestedModel',{
    'param1': fields.Integer()
}, description='example nested model')


example_input_model = api.model('ExampleInput', {
    'floatparam': fields.Float(description='Description of parameter', required=False, example=7.0, default=7.0),
    'intparam': fields.Integer(description='Description of parameter', required=True, example=10),
    'strparam': fields.String(description='Description of parameter', required=True, example='example'),
    'dtparam': fields.DateTime(dt_format='iso8601', description='Description of parameter', required=True, example='2021-07-21T19:37:06+0000'),
    'nestedparam': fields.Nested(example_nested_model, skip_none=True, allow_null=False, description='Descripcion of parameter'),
    'listparam': fields.List(fields.Integer(),description="Description of parameter", example=[1,2,3])
}, description="Example input model")


example_output_model = api.model('ExampleOutput', {
    'param1': fields.Float(description='Description of parameter', required=True, example=1.0),
    'param2': fields.Float(description='Description of parameter', required=True, example=1.0)
}, description="Example output model")


chatbot_input_model = api.model('ChatbotInput',{
    'question': fields.String(description = 'Question to chatbot', required = True, example = 'Hola')
}, description = 'Chatbot Input Model')

chatbot_output_model = api.model('ChatbotOutput', {
    'response': fields.String(description = 'chatbot response', required = True, example = 'Hola! ¿Cómo puedo ayudarte hoy?'),
    'execution_time': fields.Float(description = 'time taken to process the request', required = False, example = 0.054)
})

