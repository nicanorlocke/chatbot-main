#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute @tobeal on GitHub)

import time
import threading

from flask import Response, request
from flask_restx import Resource

from chatbot_api import logger
from chatbot_api.api.v1 import api
from chatbot_api.core import cache, limiter
from chatbot_api.utils import handle400error, handle404error, handle500error

from chatbot_api.api.example_parsers import example_parser, chatbot_parser, chatbot_chat_parser

from chatbot_api.model.chat_bot import Chatbot
from chatbot_api.api.example_models import chatbot_input_model, chatbot_output_model


model = Chatbot()
example_ns = api.namespace('chatbot', description='Chatbot namespace')


@example_ns.route('/')
class ExamplePrediction(Resource):
    
    @api.expect(chatbot_input_model)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(chatbot_output_model, code=200, description='OK', as_list=False)
    @limiter.limit('1000000/hour') 
    @cache.cached(timeout=1, query_string=True)
    def post(self):
        """
        Send message to chatbot and get response
        """
        global model
        
        # check parameters
        try:
            params = chatbot_parser.parse_args()
            logger.info(params)
        except:
            return handle400error(example_ns, 'Malformed request. Please, check the request at /v1')

        try:
            
            output = model.get_response(params['question'])
            logger.info(output)

            result = {'response': output}
            return result

        except Exception as e:
            logger.error(handle500error(example_ns, "Unhandled errors"))
            return handle500error(example_ns, 'Malformed request. Please, check the request at /v1')



@example_ns.route('/speed_test')
class SpeedTest(Resource):
    
    @api.expect(chatbot_input_model)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(chatbot_output_model, code=200, description='OK', as_list=False)
    @limiter.limit('1000000/hour') 
    @cache.cached(timeout=1, query_string=True)
    def post(self):
        """
        Send message to chatbot and check speed for response
        """
        global model
        start_time = time.perf_counter()
        
        # check parameters
        try:
            params = chatbot_parser.parse_args()
            logger.info(params)
        except:
            return handle400error(example_ns, 'Malformed request. Please, check the request at /v1')

        try:

            def model_respone ():
                return model.get_response(params['question'])

            thread = threading.Thread(target=model_respone)
            thread.start()
            thread.join()

            response = model.get_response(params['question'])  # Simulate your model's response
            end_time = time.perf_counter()
            execution_time = end_time - start_time

            result = {'response': response, 'execution_time': execution_time}
            return result

        except Exception as e:
            logger.error(handle500error(example_ns, "Unhandled errors"))
            return handle500error(example_ns, 'Malformed request. Please, check the request at /v1')







@example_ns.route('/chat')
class SSEChat(Resource):
    
    @api.expect(chatbot_input_model)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @limiter.limit('1000000/hour')
    def get(self):
        """
        Send message to chatbot and get response by SSE
        """
        global model
        
        # check parameters
        try:
            params = chatbot_chat_parser.parse_args()
            logger.info(params)

            # params = request.args
            # question = params.get('question', '')
            # if not question:
            #     return {'response': 'Invalid parameters: question is required'}, 400
        except:
            return handle400error(example_ns, 'Malformed request. Please, check the request at /v1')

        try:
            output = model.get_chat_response(params['question'])
            logger.info(output)
            return Response(output, content_type='text/event-stream')

        except Exception as e:
            logger.error(handle500error(example_ns, "Unhandled errors"))
            return handle500error(example_ns, 'Malformed request. Please, check the request at /v1')
