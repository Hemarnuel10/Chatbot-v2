from Services.history_service import historyService
from Services.prompt_builder import build_prompt
from provider.provider_manager import ProviderManager

class ChatService:

    def chat(self, user_message):
        
        # Load previous conversation
        recent_conversation = historyService.get_recent_history(10)

        # Build prompt
        full_prompt = build_prompt(
            recent_conversation,
            user_message
        )

        # Get current AI provider
        provider = ProviderManager.get_provider()
        
        # Generate response
        ai_response = provider.generate(full_prompt)

        conversation = Conversation(user_message, ai_response, provider)

        historyService.save_chat(conversation)
        

        # Return response
        return ai_response