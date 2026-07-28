from config import APP_NAME
from others.commands  import show_help, show_about, commands
from others.utils import show_heading
from Services.chat_service import ChatService

show_heading(APP_NAME)

chat_service = ChatService()

while True:
    user_message = input("You: ")

    if user_message.lower() in commands:
        commands[user_message.lower()]()
        continue

    elif user_message.lower() == "/exit":
        print("\n👋 Goodbye!")                     
        #logger.info("Application closed by user.")
        break
        
    else:
         response = chat_service.chat(user_message)
         print(response)