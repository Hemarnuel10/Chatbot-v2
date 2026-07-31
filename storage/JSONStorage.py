import json

class JsonStorage:
    
    FILE = "chat_storage.json"
    
    def load_storage(self):
        try:
            with open(self.FILE, "r") as file:
                content = json.load(file)
                return content
        except FileNotFoundError:
            return []
        
    def load_recent(self, limit):
        full_storage = self.load_storage()
        return full_storage[-limit:]
        
    def save(self, conversation):
        history = self.load_storage()

        history.append(conversation.to_dict())

        with open(self.FILE, "w") as file:
            json.dump(history, file, indent=4)
            
            
    def clear_storage(self):
            content = []
            with open(self.FILE, "w") as file:
                json.dump(content, file, indent=4)
            
    
        