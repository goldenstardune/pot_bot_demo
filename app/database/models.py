#tresc bazy dannych orn
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3') #szbd

async_session = async_sessionmaker(engine) #podlaczenie 

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str] = mapped_column(String(25))
    second_name: Mapped[str] = mapped_column(String(25))
    number: Mapped[str] = mapped_column(String(15))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
