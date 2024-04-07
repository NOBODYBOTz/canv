from typing import cast

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Message, Update, User
from telegram.ext import ContextTypes
from telegram.helpers import mention_html

from Assistant.database.block_db import is_banned_user
from Assistant.database.users_db import add_served_user
from config import LOGGER_ID, OWNER_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = cast(User, update.effective_user)
    message = cast(Message, update.effective_message)
    owner = await context.bot.get_chat(OWNER_ID)
    if await is_banned_user(message.from_user.id):
        return
        
    await add_served_user(message.from_user.id)
    await context.bot.send_message(
        chat_id=LOGGER_ID,
        text=f"<b>ɴᴇᴡ ᴜsᴇʀ :</b>\nᴜsᴇʀ: {mention_html(user.id, user.first_name)}\n<b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{user.username}\n<b>ɪᴅ:</b> <code>{user.id}</code>",
    )
    await message.reply_text(
        
        text=f"ʜᴇʟʟᴏ {mention_html(user.id, user.first_name)}.😌\n\nYou can contact me using this bot.\n\n<b>Send <code>Hello</code> I will Reply Soon...</b>",
    )
    return
