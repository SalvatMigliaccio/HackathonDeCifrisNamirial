from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).filter(User.Username == username))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: User):
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
