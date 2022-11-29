import logging

from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
def translit(text):
    symbol_dict = { 'А':'A', 
                    'Б':'B', 
                    'В':'V', 
                    'Г':'G', 
                    'Д':'D',
                    'Е':'E',
                    'Ё':'E',
                    'Ж':'Zh',
                    'З':'Z',
                    'И':'I',
                    'Й':'I',
                    'К':'K',
                    'Л':'L',
                    'М':'M',
                    'Н':'N',
                    'О':'O',
                    'П':'P',
                    'Р':'R',
                    'С':'S',
                    'Т':'T',
                    'У':'U',
                    'Ф':'F',
                    'Х':'Kh',
                    'Ц':'Ts',
                    'Ч':'Ch',
                    'Ш':'Sh',
                    'Щ':'Shch',
                    'Ы':'Y',
                    'Ъ':'Ie',
                    'Э':'E',
                    'Ю':'Iu',
                    'Я':'Ia',
                    'Ь':'',
                    'а':'a',
                    'б':'b',
                    'в':'v',
                    'г':'g',
                    'д':'d',
                    'е':'e',
                    'ё':'e',
                    'ж':'zh',
                    'з':'z',
                    'и':'i',
                    'й':'i',
                    'к':'k',
                    'л':'l',
                    'м':'m',
                    'н':'n',
                    'о':'o',
                    'п':'p',
                    'р':'r',
                    'с':'s',
                    'т':'t',
                    'у':'u',
                    'ф':'f',
                    'х':'kh',
                    'ц':'ts',
                    'ч':'ch',
                    'ш':'sh',
                    'щ':'shсh',
                    'ъ':'ie',
                    'ы':'y',
                    'ь':'',
                    'э':'e',
                    'ю':'iu',
                    'я':'ia',}
    tr = ''
    for i in text:
        if i in symbol_dict.keys():
            tr += symbol_dict.get(i)
        else:
            tr += i
    
    return tr.upper()

@dp.message_handler(commands=['start'])
async def send_welcome(message : types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Привет, {user_name}! Введи своё ФИО"

    logging.info(f"{user_name=} {user_id} sent message: {message.text}")
    await message.reply(text)
    
    


@dp.message_handler()
async def send_echo(message : types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = translit(message.text)

    logging.info(f"{user_name=} {user_id} sent message: {text}")
    await bot.send_message(user_id, text)



if __name__ == "__main__":
    executor.start_polling(dp)
