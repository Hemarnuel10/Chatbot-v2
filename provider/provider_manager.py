from config import PROVIDER

providers = {
    gemini : show_help,
    deepseek : show_about,
    claude : show_history,
    openai: show_version,
    grok : show_clear
}

if PROVIDER in providers:
    print("provider available")
else:
    print("provider not available")