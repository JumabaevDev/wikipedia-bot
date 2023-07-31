from aiogram import Bot,Dispatcher,executor,types
import wikipedia


bot = Bot("YOUR_TOKEN")

dp = Dispatcher(bot=bot,parse_mode=types.ParseMode.HTML)

@dp.message_handler(commands=['start'])
async def start_cmd(message:types.Message):
    await message.answer(f"{message.from_user.full_name}, welcome to Wikipedia bot!")

@dp.message_handler(content_types=['text'])
async def get_wiki(message: types.Message):
    try:
        query = message.text
        wikipedia.summary(query
    except :
        await message.answer("<b>⚠️Error: Could not find information</b>")
