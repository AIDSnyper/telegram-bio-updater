from pyrogram import Client
from datetime import datetime
import os

# Load API credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

# Set your preferred timezone
your_timezone = "Asia/Tashkent"  # Change this to your time zone

# Get the correct time
tz = pytz.timezone(your_timezone)
now = datetime.now(tz).strftime("%H:%M")

# Update Telegram bio
with Client("my_account", api_id=api_id, api_hash=api_hash, session_string=session_string) as app:
    bio_text = f"Is not it {now}?"
    app.update_profile(bio=bio_text)
    print(f"Updated bio to: {bio_text}")
