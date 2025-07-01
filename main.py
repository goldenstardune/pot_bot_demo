import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import InputSticker
from app.handlers import router
from app.database.models import async_main


async def main():
	await async_main()
	bot = Bot(token='mytoken') 
	dp = Dispatcher()
	dp.include_router(router) #wlaczycz router 
	await dp.start_polling(bot)

if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print('I\'m unavailable right now. Let\'s chat later.')
