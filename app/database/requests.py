from sqlalchemy import select
from .models import async_session, User

async def get_user(tg_id: int) -> User | None:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        return result.scalar_one_or_none()

async def create_or_update_user(tg_id: int, **kwargs):
    async with async_session() as session:
        user = await get_user(tg_id)
        if not user:
            user = User(tg_id=tg_id)
            session.add(user)
        for key, value in kwargs.items():
            setattr(user, key, value)
        await session.commit()
