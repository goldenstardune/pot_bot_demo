import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


from app import router  #handlers
from app.database.models import init_db #bd
from app.middleware.antispam import RegistrationAntiSpamMiddleware

# .env
load_dotenv()

async def main() -> None:
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("BOT_TOKEN nie znaleziony w pliku .env!")

    bot = Bot(
        token=bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    #middleware
    dp.message.outer_middleware(RegistrationAntiSpamMiddleware(limit=5, period=3600))

    #router
    dp.include_router(router)

    await init_db()
    print("Data baze is ready")

    print("Bot started!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nI'm unavailable right now. Let's chat later.")
