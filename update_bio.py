from pyrogram import Client
from datetime import datetime
import os

# Load API credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

with Client("my_account", api_id=api_id, api_hash=api_hash, session_string=session_string) as app:
    now = datetime.now().strftime("%H:%M")
    bio_text = f"Is not it {now}?"
    
    app.update_profile(bio=bio_text)
    print(f"Updated bio to: {bio_text}")
