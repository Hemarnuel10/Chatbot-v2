from datetime import datetime
from storage.storage_manager import StorageManager

class Conversation:
    def __init__(self, user_message, ai_message, provider):
        self.user_message = user_message
        self.ai_message = ai_message
        self.provider = provide.model
        self.timestamp = datetime.now()