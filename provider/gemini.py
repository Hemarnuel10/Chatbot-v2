from google import genai
from config import API_KEY, MODEL

client = genai.Client(api_key=API_KEY)

def get_response(full_prompt):
    interaction = client.interactions.create(
        model=MODEL,
        input=full_prompt
    ) 
    response = interaction.output_text
    return response


