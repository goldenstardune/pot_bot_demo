from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select

async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id, first_name="", second_name="", number=""))
            await session.commit()

async def save_user_data(tg_id: int, first_name: str, second_name: str, number: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            user = User(
                tg_id=tg_id,
                first_name=first_name,
                second_name=second_name,
                number=number
            )
            session.add(user)
        else:
            user.first_name = first_name
            user.second_name = second_name
            user.number = number
        await session.commit()