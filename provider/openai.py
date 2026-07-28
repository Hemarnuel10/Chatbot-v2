from openai import OpenAI
from config import API_KEY, MODEL

client = OpenAI(api_key=API_KEY)

def get_response(full_prompt):
    response = client.responses.create(
        model=MODEL,
        input=full_prompt
    )
    
    ai_response = response.output_text
    return ai_response