from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models import User

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).filter(User.Username == username))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: User):
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_me(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.UID == user_id))
    return result.scalars().first()

async def delete_user(db: AsyncSession, user: User):
    db.delete(user)
    await db.commit()
    
async def update_user(db: AsyncSession, user: User):
    db.add(user)
    await db.commit()
    await db.refresh(user)
    


