#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id=12336381, #get it from https://my.telegram.org/auth
    api_hash="d277ad89dc55879cf67455ac9733db3b", #get it from https://my.telegram.org/auth
    bot_token="5251775394:AAFAwhzb7BKCxl9mtY0ah7wjPMSlIRFD7Nc", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        