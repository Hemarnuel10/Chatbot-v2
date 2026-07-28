from config import PROVIDER
from provider.gemini import get_response
from provider.openai import get_response

class ProviderManager:
        # self.PROVIDER = PROVIDER

    def get_provider(self):
        if PROVIDER in providers:
            return PROVIDER
        else:
            print("provider not available")
            raise ValueError(f"Unsupported AI provider: {PROVIDER}")

providers = {
    "gemini" : get_response,
    "openai" : get_response

}

