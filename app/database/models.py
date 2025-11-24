#tresc bazy dannych orn
from sqlalchemy import BigInteger, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3") #szbd
async_session = async_sessionmaker(engine, expire_on_commit=False) #podlaczenie 

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    second_name: Mapped[str] = mapped_column(String(50), nullable=True)
    number: Mapped[str] = mapped_column(String(20), nullable=True)
    registered_at: Mapped[int] = mapped_column(Integer, default=lambda: int(__import__("time").time()))

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
