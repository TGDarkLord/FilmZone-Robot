import asyncio
from pyrogram import Client as FilmZone_Robot, filters as Worker, emoji

MENTION = "{}"  
MESSAGE = "{} Welcome to {}!" 

@FilmZone_Robot.on_message(Worker.new_chat_members)
async def welcome(client, message):

    new_members = [MENTION.format(message.from_user.mention) for i in message.new_chat_members]

    text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))

    dell=await message.reply_text(text, disable_web_page_preview=True)
    await asyncio.sleep(10)
    await dell.delete()
