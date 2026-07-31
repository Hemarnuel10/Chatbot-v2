from config import APP_NAME, VERSION, MODEL, DEVELOPER
from Services.history_service import historyService
from others.utils import show_heading


def show_help():
    print("""Commands:
- /help : Show available commands
- /about : About Emma AI
- /history : Show conversation history
- /version : Show application version
- /model : Show current AI model
- /clear : Clear the conversation history
- /exit : Close the chatbot
-/stats : Check AI stats
""")


def show_about():
    show_heading(APP_NAME)
    print(f"""
Version: {VERSION}

Developer:
{DEVELOPER}

Purpose:
A personal AI assistant for learning
Programming, AI, Aerospace Engineering,
Mathematics and Technology.

AI Model:
{MODEL}

Status:
Online
""")


def show_history():
    history = historyService.load_history()

    if not history:
        print("No conversation history found.")
        return

    show_heading("Conversation History")
    print("\n".join(history))


def show_version():
    show_heading(APP_NAME)
    print(f"Version: {VERSION}")


def show_clear():
    while True:
        confirm = input(
            "Are you sure you want to clear the conversation history? (y/n): "
        ).lower()

        if confirm in ["y", "yes"]:
            historyService.clear_history()
            print("Conversation history cleared successfully.")
            break

        elif confirm in ["n", "no"]:
            print("Operation cancelled.")
            break

        else:
            print("Please enter only 'y' or 'n'.")


def show_model():
    show_heading(APP_NAME)
    print(f"Model: {MODEL}")

def show_stats():
    show_heading(f"{APP_NAME} Statistics" )
    history = historyService.load_history()
    if len(history) > 0:
        print(f"\nTotal Conversations: {len(history)}\nFirst Chat: {history[0]["Timestamp"]}\nLast Chat: {history[-1]["Timestamp"]}\nModel Used: {MODEL}")
    else:
        print("No Stats yet")

commands = {
    "/help": show_help,
    "/about": show_about,
    "/history": show_history,
    "/version": show_version,
    "/clear": show_clear,
    "/model": show_model,
    "/stats" : show_stats
}