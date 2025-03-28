#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute @tobeal on GitHub)


from pydantic import BaseModel, Field


#Pydantic model for input data
class ExampleInput(BaseModel):
    question: str = Field(..., min_length=3, description='Send a question for the chatbot to respond', example = 'hola')


#Pydantic model for output data
class ExampleOutput(BaseModel):
    response: str = Field(..., min_length=3, description='Chatbot response', example = '¡Hola! ¿Cómo puedo ayudarte hoy?')
    execution_time : float = Field(default=None, description = 'response time', example = 0.5)
