#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20351304"))
API_HASH = environ.get("API_HASH", "c09d07f9c0600cdc2f6eef07130df8e1")
BOT_TOKEN = environ.get("BOT_TOKEN", "7264896037:AAHZ0ABhEFDQqHPTmxk6GYtEuOLQ5SgQa6A")
OWNER = int(environ.get("OWNER", ""))
CREDIT = "𝄟⃝‌🐬🇳‌KAPIL𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
