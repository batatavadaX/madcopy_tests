import os

from pyrogram import Client, filters
from pyrogram.types import Message

BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')

m = Client("m", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@m.on_message(filters.command("set", prefixes="/"))
async def set_cookie(Client, m: Message):
    text=m.input_str
    if not text:
      await m.reply("ENTER URL")
      return
    filename=f"{await m.from_user.id}.txt"
    with open(filename, "w") as myp:
      myp.write(text)
    myp.close()
    await m.reply("Cookies Saved")
    
@m.on_message(filters.command("show", prefixes="/"))
async def show_cookie(Client, m: Message):
    await m.reply("lol")
@m.on_message(filters.command("copy", prefixes="/"))
async def copy_(Client, m: Message):
    await m.reply("lol")

m.run()
