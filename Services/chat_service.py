from Services.history_service import save_chat, get_recent_history
from Services.prompt_builder import build_prompt

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
        provider = ProviderManager.get_provider()

        # Generate response
        ai_response = provider.generate(full_prompt)

        # Save chat
        save_chat(
            user_message,
            ai_response,
            provider.model
        )

        # Return response
        return ai_response