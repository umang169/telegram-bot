from telethon import TelegramClient, events
import os

# Load API credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

# Define the session
client = TelegramClient("bot_session", api_id, api_hash)

# Define source channel and target bot
source_channel = os.getenv("SOURCE_CHANNEL")
target_bot = os.getenv("TARGET_BOT")

@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    await client.send_message(target_bot, event.message)

print("Bot is running...")
client.start()
client.run_until_disconnected()
