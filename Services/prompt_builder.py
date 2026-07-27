#read system prompt
with open("system_prompt.txt", "r") as file:
    system_prompt = file.read()
    
def build_prompt(conversation, user_message):
    full_prompt = (
        f"{system_prompt}\n\n"
        f"{conversation}\n\n"
        f"User: {user_message}"
    )
    return full_prompt