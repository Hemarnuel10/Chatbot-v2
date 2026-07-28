from Services.history_service import save_chat, get_recent_history
from Services.prompt_builder import build_prompt
from provider.provider_manager import ProviderManager
class ChatService:

    def chat(self, user_message):
        
        # Load previous conversation
        conversation = get_recent_history(10)

        # Build prompt
        full_prompt = build_prompt(
            conversation,
            user_message
        )

        # Get current AI provider
        provider = ProviderManager().get_provider()
        print(f"provider gotten sucessfull: {provider}")
        # Generate response
        ai_response = provider.get_response(full_prompt)
        print("ai response gotten sucessfully")
        

        # Save chat
        save_chat(
            user_message,
            ai_response,
            provider.model
        )

        # Return response
        return ai_response