from google import genai
from config import API_KEY, MODEL

client = genai.Client(api_key=API_KEY)

def ask_ai(full_prompt):
    response = client.responses.create(
        model=MODEL,
        contents=full_prompt
    )
    
    ai_response = response.output_text
    return ai_response

from openai import OpenAI

client = OpenAI()

response = client.responses.create(model="gpt-5.6",
input="Write a short bedtime story about a unicorn.")

print(response.output_text)