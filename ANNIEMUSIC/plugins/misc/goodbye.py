from pyrogram import filters
from ANNIEMUSIC import app

@app.on_message(filters.command("goodbye", prefixes=["/", "!"]))
async def farewell_message(client, message):
    message_text = """
    Radhe Radhe 💗
    """
    await message.reply_text(message_text)
