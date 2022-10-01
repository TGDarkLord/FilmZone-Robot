import asyncio 

from pyrogram import Client as filmzone_robot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserIsBlocked, PeerIdInvalid

from FilmZone_Robot.admins.index_files import index_files_to_db
from FilmZone_Robot.database.autofilter_db import get_file_details
from FilmZone_Robot.database._utils import get_size, is_subscribed
from FilmZone_Robot.database._utils import lucifer_temp

from translation import FilmZone
from config import BUTTONS, FORCES_SUB, CUSTOM_FILE_CAPTION, START_MSG, DEV_NAME, bot_info, ADMINS, team_name, team_link

from FilmZone_Robot.modules._text_ import module

lock = asyncio.Lock()

@filmzone_robot.on_callback_query()
async def cb_handler(client: filmzone_robot, query):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id

    if (clicked == typed):

# # ---------- 🔘 [ | 𝗚𝗥𝗢𝗨𝗣 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- # #

        if query.data.startswith("nextgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backgroup_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 CHECK MY PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# # ---------- 🔘 [ | 𝗕𝗢𝗧 𝗣𝗠 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- # #


        elif query.data.startswith("nextbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backbot_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("Close 🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- 📁 [ | 𝗚𝗘𝗧 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data.startswith("filmzone_robot"):
            ident, file_id = query.data.split("#")
            files_ = await get_file_details(file_id)
            if not files_:
                return await query.answer('No such file exist.')
            files = files_[0]
            title = files.file_name
            size=get_size(files.file_size)
            caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, size=size, caption=files.caption)

            try:
                if FORCES_SUB and not await is_subscribed(client, query):
                    await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
                    return
                else:
                    await client.send_cached_media(
                        chat_id=query.from_user.id,
                        file_id=file_id,
                        caption=caption
                        )
                    await query.answer('🤖 Check PM, I have Sent Files In Pm 🤖',show_alert = True)
            except UserIsBlocked:
                await query.answer('Unblock the bot mahn !',show_alert = True)
            except PeerIdInvalid:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
            except Exception as e:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")

# ---------- 📁 [ | 𝗣𝗠 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #

        elif query.data.startswith("pmfile"):
            if FORCES_SUB and not await is_subscribed(client, query):
                await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒",show_alert=True)
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=get_size(files.file_size)
                
                caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, size=size, caption=files.caption)

                buttons = [[
                  InlineKeyboardButton('🧑‍💻 How To Own 🧑‍💻', url='https://t.me/Mo_Tech_Group')
                  ]]                 
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )


# ---------- 📁 [ | 𝗠𝗢𝗗𝗨𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data == "start":
            buttons = [[
                InlineKeyboardButton("🔗 Film Zone", url=f"https://t.me/+bTrA63X_d2I3MDVl")
                ],[
                InlineKeyboardButton("ℹ️ Help", callback_data="help"),
                InlineKeyboardButton(text="😎 About", callback_data="crpf") 
                ]]  
            await query.message.edit(text=FilmZone.START_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "help":
            buttons = [[
                InlineKeyboardButton('🚨 Alive', callback_data='alive'),
                InlineKeyboardButton('🔍 IMDB', callback_data='search'),
                InlineKeyboardButton('🔗 Link', callback_data='link'),
                ],[
                InlineKeyboardButton('⚠️ Faq', callback_data='faq'),
                InlineKeyboardButton('🆔 Ids', callback_data='info'),
                InlineKeyboardButton('🎼 Song', callback_data='music'),
                ],[
                InlineKeyboardButton(text='😎 About', callback_data='crpf'),
                InlineKeyboardButton('🏠 Home', callback_data='start'),
                InlineKeyboardButton('❎ Close', callback_data='close_data'),
                ]]
            await query.message.edit(text=FilmZone.HELP_MSG.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif "crpf" in query.data:
            return await query.answer("""
꧁֍FILM ZONE BOT֍꧂

🤴 Creator: DarkLord
❖ Language: Python3
❖ Hosted: Heroku 
❖ Version: 2.0.1 [BETA]
❖ Farmework: Pyrogram
❖ Database: MongoDB
֎ Bot: Indian 🇮🇳
""", show_alert=True)
        
        elif query.data == "alive":
            buttons = [[ 
                InlineKeyboardButton('🔙 Back', callback_data="help") 
                ]]
              await query.message.edit(text=FilmZone.ALIVE_MSG.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
        elif query.data == "search":
            buttons = [[
                InlineKeyboardButton('🔙 Back', callback_data='help')
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=FilmZone.SEARCH_MSG,
                disable_web_page_preview=True,
                reply_markup=reply_markup,
                parse_mode='html'
        )
        elif query.data == "link":
            buttons = [[
                InlineKeyboardButton('🔙 Back', callback_data='help')
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=FilmZone.LINK_MSG,
                disable_web_page_preview=True,
                reply_markup=reply_markup,
                parse_mode='html'
        )       
        elif query.data == "info":
            buttons = [[
            InlineKeyboardButton('🔙 Back', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=FilmZone.INFO_MSG,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
