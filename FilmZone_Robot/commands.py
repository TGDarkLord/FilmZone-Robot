from random import choice
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as FilmZone_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import FilmZone
from FilmZone_Robot.database.users_chats_db import db

@FilmZone_Robot.on_message(Worker.command(["start"]))
async def start_message(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton("🔗 Film Zone", url=f"https://t.me/+bTrA63X_d2I3MDVl")
            ],[
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
            InlineKeyboardButton(text="😎 About", callback_data="crpf") 
            ]]
        await message.reply_photo(photo = choice(BOT_PICS), caption=START_MSG.format(mention = message.from_user.mention, bot_name = bot_info.BOT_NAME, bot_username = bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons)
        )
        return 

    elif len(message.command) ==2 and message.command[1] in ["subscribe"]:
        FORCES=["https://telegra.ph/file/b2acb2586995d0e107760.jpg"]
        invite_link = await bot.create_chat_invite_link(int(FORCES_SUB))
        button=[[
         InlineKeyboardButton("🔔 SUBSCRIBE 🔔", url=invite_link.invite_link)
         ]]
        reply_markup = InlineKeyboardMarkup(button)
        await message.reply_photo(
            photo=choice(FORCES),
            caption=f"""<i><b>Hello {message.from_user.mention}. \nYou Have <a href="{invite_link.invite_link}">Not Subscribed</a> To <a href="{invite_link.invite_link}">My Update Channel</a>.So you do not get the Files on Inline Mode, Bot Pm and Group</i></b>""",
            reply_markup=reply_markup
        )
        return
  
    if len(message.command) == 2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        buttons = [[
            InlineKeyboardButton("🔗 Film Zone", url=f"https://t.me/+bTrA63X_d2I3MDVl")
            ],[
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
            InlineKeyboardButton(text="😎 About", callback_data="crpf") 
            ]]
        await message.reply_photo(photo = choice(BOT_PICS), caption=START_MSG.format(mention = message.from_user.mention, bot_name = bot_info.BOT_NAME, bot_username = bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons))
