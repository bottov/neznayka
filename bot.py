#!venv/bin/python

import os

from telethon.sync import TelegramClient, events
from telethon.errors.rpcerrorlist import *

from Models.user import *
from Models.message import *

from lib import *

from dotenv import load_dotenv

# Initialize bot and... just the bot!
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

bot = TelegramClient('neznayka', api_id, api_hash).start(bot_token=bot_token)

# Обработка всех сообщений
@bot.on(events.NewMessage())
async def echo_all(event):

    user = await get_user(event)
    if event.text == '/start':
        await event.respond('Я чат-бот Незнайка, поболтаем? 😈')
    elif not event.text:
        pass
    else:
        # сообщение пользователя
        print(f'{user.first_name}:', event.text)
        
        word = last_word(event.text)
        message = Message.select().where(Message.text ** f'%{word}%').order_by(Message.id.desc()).get_or_none()
        Message.create(chat_id=user.chat_id, text=event.text)
        if message:
            # ответ незнайки
            reply = Message.select().where(Message.id < message.id).order_by(Message.id.desc()).get()
            Message.create(chat_id=1, text=reply.text)
            await event.reply(reply.text)
            print('Незнайка:', reply.text)
            print()
    
    database.close()

# Бот
if __name__ == '__main__':
    
    bot.run_until_disconnected()
