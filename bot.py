import os
from telethon import TelegramClient

# Fetching credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

client = TelegramClient("session_name", api_id, api_hash)

async def main():
    await client.start(phone_number)
    print("Client is running...")

with client:
    client.loop.run_until_complete(main())
