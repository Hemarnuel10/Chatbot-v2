from config import PROVIDER
from provider.gemini import GeminiProvider
from provider.openai import OpenaiProvider

providers = {
    "gemini" : GeminiProvider,
    "openai" : OpenaiProvider
}

class ProviderManager:
        @staticmethod

        def get_provider():
            if PROVIDER not in providers:
                raise ValueError(f"Unsupported provider: {PROVIDER}")
    
            return providers[PROVIDER]()


