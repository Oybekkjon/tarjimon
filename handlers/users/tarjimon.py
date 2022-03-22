from aiogram import types
from googletrans import Translator
from loader import dp
tarjimon = Translator()

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    matn = message.text
    til = tarjimon.detect(message.text).lang
    if til == 'uz':
        tarjima = tarjimon.translate(matn, dest='en', src='uz')
        await message.answer(text=f'{tarjima.text}')
    else:
        tarjima = tarjimon.translate(matn, dest='uz', src='en')
        await message.answer(text=f'{tarjima.text}')
