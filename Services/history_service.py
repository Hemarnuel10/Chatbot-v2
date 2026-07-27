#from config import SEPARATOR
import json
from datetime import datetime
def save_chat(user_message, ai_message, model):
        history = load_history()
        content = {
            "Id" : len(history) + 1,
            "User" : user_message,
            "AI" : ai_message,
            "Model" : model,
            "Timestamp": datetime.now().isoformat()
        }
        
        history.append(content)
        with open("chat_history.json", "w") as file:
            json.dump(history, file, indent=4)
        

def load_history():
    try:
        with open("chat_history.json", "r") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        return []
        
def clear_history():
    content = []
    with open("chat_history.json", "w") as file:
        json.dump(content, file, indent=4)
        
def get_recent_history(limit):
    chat_history = load_history()
    recent_history = chat_history[-limit:]
    conversation = ""
    for chat in recent_history:
        user= chat["User"]
        ai= chat["AI"]
        conversation += f"\nUser: {user}\nAI: {ai}"
    return conversation
        