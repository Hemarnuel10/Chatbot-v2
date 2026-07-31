from openai import OpenAI
from config import API_KEY, MODEL

client = OpenAI(api_key=API_KEY)

class OpenaiProvider:
    def __init__(self):
        self.model = MODEL

    def generate(self, full_prompt):
        interaction = client.interactions.create(
            model=MODEL,
            input=full_prompt
        ) 
        response = interaction.output_text
        return response
