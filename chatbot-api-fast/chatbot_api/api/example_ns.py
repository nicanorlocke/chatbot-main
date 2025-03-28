#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute @tobeal on GitHub)

import time
import threading

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse

from chatbot_api import logger
from chatbot_api.utils import handle400error, handle404error, handle500error

from chatbot_api.model.chat_bot import Chatbot
from chatbot_api.api.example_models import ExampleInput, ExampleOutput

chat_bot_ns = APIRouter()

model = Chatbot()


@chat_bot_ns.get('/', response_model = ExampleOutput)
def example_get(input_param: ExampleInput = Depends()) :
    """
        Check behaviour
    """
    
    try:
        output = model.get_response(input_param)
        logger.info(output)
        return {"model_output": output}
    
    except Exception as e:
        logger.error(handle500error(chat_bot_ns, "Unhadled errors"))
        raise HTTPException(status_code=500, detail = f"Unhadled errors: {e}")



@chat_bot_ns.post('/', response_model = ExampleOutput)
def example_post(input_data: ExampleInput):
    """
        Perfoming a processing
    """

    try:

        output = model.get_response(input_data.question)
        logger.info(output)
        return {"response": output}
    
    except Exception as e:
        logger.error(handle500error(chat_bot_ns, "Unhandled errors"))
        raise HTTPException(status_code=500, detail = f"Unhandle errors: {e}")



@chat_bot_ns.post('/speed_test', response_model = ExampleOutput)
def example_post(input_data: ExampleInput):
    """
        Perfoming a processing
    """

    start_time = time.perf_counter()

    try:
        def model_response():
            return model.get_response(input_data.question)
    
        thread = threading.Thread(target=model_response)
        thread.start()
        thread.join()

        response = model.get_response(input_data.question)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        return {"response": response, "execution_time": execution_time}
    
    except Exception as e:
        logger.error(handle500error(chat_bot_ns, "Unhandled errors"))
        raise HTTPException(status_code=500, detail = f"Unhandle errors: {e}")
    






@chat_bot_ns.get("/chat/stream")
async def chat(question: str):
    """
        Send question to chatbot & wait for response
    """

    try:
        response_generator = model.get_chat_response(question)
        return StreamingResponse(response_generator, media_type="text/event-stream")
    
    except Exception as e:
        logger.error(handle500error(chat_bot_ns, f"Unhandled errors {e}"))
        raise HTTPException(status_code=500, detail = f"Unhandle error: {e}")

