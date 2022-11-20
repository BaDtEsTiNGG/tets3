
import time
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
import sqlite3 as sq
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram import types
import json
import asyncio
import requests
import random
import aiohttp





REFERAL = "Staff_hunter_bot"
saportUSERNAME = "@SAPORT"
storage = MemoryStorage()
TOKEN = "5451896391:AAHwNHZ450X92xVg9_T6-xenAADNQHoyCjc"
proxy_url = 'socks5://185.239.138.200:8000'
proxu_auth = aiohttp.BasicAuth(login='KRbkpY',password='J3shW3')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
############################################          ООП ? нет ,не слышал!

TiketChat = -1001752467023
WorkerChat = -1001852933289
StuffChat = -847405161




class FSMAdmin(StatesGroup):
    name = State()
    prise = State()
    city = State()
    region = State()
class FSMPay(StatesGroup):
    Pay = State()
class FSMtiket(StatesGroup):
    text = State()
    photo = State()
async def on_startup(_):
    print('BOT ON')



"""главное меню """
@dp.message_handler(content_types=["text"])
async def start(message):
    

        await bot.send_message(message.from_user.id, "test")





executor.start_polling(dp, skip_updates=True, on_startup=on_startup)#
