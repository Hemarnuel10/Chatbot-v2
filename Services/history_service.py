#from config import SEPARATOR
import json
from storage.storage_manager import StorageManager

class historyService:

    storage = StorageManager.get_storage()
    
    def save_chat(self, conversation):
        self.storage.save(conversation)
            
    def load_history(self):
        self.storage.load_storage()
            
    def clear_history(self):
        self.storage.clear_storage()
              
    def get_recent_history(self,limit):
            storage_history = self.storage.load_recent(limit)
            conversation = ""
            for chat in storage_history:
                user= chat["User"]
                ai= chat["AI"]
                conversation += f"\nUser: {user}\nAI: {ai}"
            return conversation
        