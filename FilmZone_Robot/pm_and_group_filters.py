from pyrogram import Client as FilmZone_Robot, filters as Worker
from FilmZone_Robot.modules.autofilter import group_filters, pm_autofilter
from config import AUTH_GROUPS, AUTH_USERS
from FilmZone_Robot.database.users_chats_db import db


@FilmZone_Robot.on_message(Worker.text & Worker.group & Worker.incoming & Worker.chat(AUTH_GROUPS) if AUTH_GROUPS else Worker.text & Worker.group & Worker.incoming)
async def groupfilters(client, message):
    await group_filters(client, message)


@FilmZone_Robot.on_message(Worker.text & Worker.private & Worker.incoming & Worker.user(AUTH_USERS) if AUTH_USERS else Worker.text & Worker.private & Worker.incoming)
async def pm_filters(client, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
    await pm_autofilter(client, message)
