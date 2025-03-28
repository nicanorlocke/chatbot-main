from transformers import pipeline

class NLPModel:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt-2')
    
    def generate_response(self, user_input):
        response = self.generator(user_input, max_length=50, num_return_sequences=1)
        return response[0]['generated_text']
