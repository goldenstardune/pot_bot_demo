from aiogram import BaseMiddleware
from datetime import datetime, timedelta
from typing import Callable, Dict, Any, Awaitable
from aiogram.types import TelegramObject

class RegistrationAntiSpamMiddleware(BaseMiddleware):
    def __init__(self, limit: int = 5, period: int = 3600):
        self.limit = limit
        self.period = timedelta(seconds=period)
        self.attempts: Dict[int, list[datetime]] = {}

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user_id = getattr(event, "from_user", None)
        user_id = user_id.id if user_id else None
        if not user_id:
            return await handler(event, data)

        now = datetime.now()
        user_attempts = self.attempts.get(user_id, [])

        # 1 godzina
        user_attempts = [t for t in user_attempts if now - t < self.period]
        self.attempts[user_id] = user_attempts

        # blokada po 5 próbach
        if len(user_attempts) >= self.limit:
            await event.answer("Too many attempts. Try again in an hour.")
            return

        state = data.get("state")
        if state:
            current_state = await state.get_state()
            if current_state and ("captcha" in current_state.lower() or "register" in current_state.lower()):
                self.attempts[user_id].append(now)
        elif hasattr(event, "message") and event.message and event.message.text == "Register":
            self.attempts[user_id].append(now)

        return await handler(event, data)
