import os
import requests

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    print("Error: TELEGRAM_BOT_TOKEN is not set.")
else:
    print("Bot token loaded successfully, ready for next step!")
  
