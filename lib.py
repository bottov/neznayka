from Models.user import *

async def get_user(event):
    user = User.get_or_none(User.chat_id==event.chat_id)
    if not user:
        user = await event.get_sender()
        user = User.create(chat_id=user.id, username=user.username, first_name=user.first_name, last_name=user.last_name)
    return user

def last_word(text):
    text = text.strip(' .,!?()')
    word = text.split()[-1]
    word = word.strip(' .,!?()')
    return word

