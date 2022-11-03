from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
HELLO KONTOL! {}
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],


@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")]