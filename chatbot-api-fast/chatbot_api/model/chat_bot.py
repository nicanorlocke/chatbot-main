
from chatbot_api import config
from chatbot_api.model.response_generator import ResponseGenerator
from chatbot_api.model.nlp_model import NLPModel

class Chatbot():
    language = str
    use_nlp = bool
    response_generator = ResponseGenerator
    nlp_model = NLPModel

    def __init__(self, language=config.DEFAULT_LANGUAGE, use_nlp=False):
        self.language = language
        self.use_nlp = use_nlp
        self.response_generator = ResponseGenerator(language)
        self.nlp_model = NLPModel() if use_nlp else None

    def set_language(self, language):
        self.language = language
        self.response_generator.set_language(language)

    def set_nlp(self, use_nlp):
        self.use_nlp = use_nlp
        if use_nlp and not self.nlp_model:
            self.nlp_model = NLPModel()

    def get_response(self, user_input):
        if self.use_nlp and self.nlp_model:
            return self.nlp_model.generate_response(user_input)
        else:
            return self.response_generator.generate_response(user_input)
    
    def get_chat_response(self, user_input):
        if self.use_nlp and self.nlp_model:
            return self.nlp_model.generate_response(user_input)
        else:
            return self.response_generator.chat_response(user_input)
