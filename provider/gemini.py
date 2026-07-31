from google import genai
from config import API_KEY, MODEL

client = genai.Client(api_key=API_KEY)

class GeminiProvider:
    def __init__(self):
        self.model = MODEL

    def generate(self, full_prompt):
        interaction = client.interactions.create(
            model=MODEL,
            input=full_prompt
        ) 
        response = interaction.output_text
        return response


