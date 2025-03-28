import pytest
import json

from chatbot_api.model.chat_bot import Chatbot

chatbot = Chatbot()

with open('test_example/chatbot_example.json', 'r') as file:
    test_data = json.load(file)


with open('chatbot_api/model/data/contexts.json', 'r') as file:
    responses = json.load(file)



@pytest.mark.parametrize('params', test_data['questionES'])
def test_chatbot_response_ES(params):
    """
    Test chatbot response for question 
    If response is on contexts responses, pass
    """

    for data in responses.get("es", []):
        if "hola" in data["questions"]:
            expected_response = data['response']
            break
    
    chatbot.set_language("es")
    result = chatbot.get_response(params)

    assert result == expected_response


@pytest.mark.parametrize('params', test_data['questionEN'])
def test_chatbot_response_EN(params):
    """
    Test chatbot response for question 
    If response is on contexts responses, pass
    """

    for data in responses.get("en", []):
        if "hello" in data["questions"]:
            expected_response = data['response']
            break
    
    chatbot.set_language("en")
    result = chatbot.get_response(params)

    assert result == expected_response