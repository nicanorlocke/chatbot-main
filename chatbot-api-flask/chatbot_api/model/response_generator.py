import json
from chatbot_api import config

class ResponseGenerator:
    def __init__(self, language=config.DEFAULT_LANGUAGE):
        self.language = language
        self.contexts = self.load_contexts(config.CONTEXT_FILE)
    
    def load_contexts(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    
    def set_language(self, language):
        if language in config.LANGUAGES:
            self.language = language
        else:
            self.language = config.DEFAULT_LANGUAGE
    
    def generate_response(self, user_input):
        for context in self.contexts.get(self.language, []):
            for question in context['questions']:
                if question.lower() in user_input.lower():
                    return context['response']
        return "I'm sorry, I don't understand that."
    

    def chat_response(self, user_input):
        response_found = False
        for context in self.contexts.get(self.language, []):
            for question in context['questions']:
                if question.lower() in user_input.lower():
                    yield f"data: {context['response']}\n\n"
                    response_found = True
        if not response_found:
            yield "I'm sorry, I don't understand that.\n\n"
        yield f"event: end\n\n"
