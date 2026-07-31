import json
import os
from dotenv import load_dotenv

load_dotenv()

with open("config.json", "r") as file:
    config = json.load(file)

# App
APP_NAME = config["app_name"]
VERSION = config["version"]
DEVELOPER = config["developer"]

# AI
PROVIDER = config["provider"]
MODEL = config["model"]
API_KEY = os.getenv("API_KEY")

# Storage
STORAGE = config["storage"]

