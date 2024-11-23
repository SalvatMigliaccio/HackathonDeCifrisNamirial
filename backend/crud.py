from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from  models import User, Operatore, Gruppo, Pratica, Documento, OperatoreGruppo

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
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
    
async def get_operator_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(Operatore).filter(Operatore.email == email))
    return result.scalars().first()

async def create_operator(db: AsyncSession, operatori: Operatore):
    db.add(operatori)
    await db.commit()
    await db.refresh(operatori)
    return operatori

async def get_operator_me(db: AsyncSession, user_id: int):
    result = await db.execute(select(Operatore).filter(Operatore.UID == user_id))
    return result.scalars().first()

async def delete_operator(db: AsyncSession, operatori: Operatore):
    db.delete(operatori)
    await db.commit()
    
async def update_operator(db: AsyncSession, operatori: Operatore):
    db.add(operatori)
    await db.commit()
    await db.refresh(operatori)
    
#defining crud for operator groups

async def get_group_by_id(db: AsyncSession, id: str):
    result = await db.execute(select(Gruppo).filter(Gruppo.id == id))
    return result.scalars().first()

async def create_group(db: AsyncSession, group: Gruppo):
    db.add(group)
    await db.commit()
    await db.refresh(group)
    return group

async def delete_group(db: AsyncSession, group: Gruppo):
    db.delete(group)
    await db.commit()   
    
async def update_group(db: AsyncSession, group: Gruppo):
    db.add(group)
    await db.commit()
    await db.refresh(group)
    
#defining crud for pratica

async def get_pratica_by_wallet_address(db: AsyncSession, wallett_address: str):
    result = await db.execute(select(Pratica).filter(Pratica.WalletAddress == wallett_address))
    return result.scalars().first()

async def create_pratica(db: AsyncSession, pratica: Pratica):
    db.add(pratica)
    await db.commit()
    await db.refresh(pratica)
    return pratica

async def delete_pratica(db: AsyncSession, pratica: Pratica):
    db.delete(pratica)
    await db.commit()
    
async def update_pratica(db: AsyncSession, pratica: Pratica):
    db.add(pratica)
    await db.commit()
    await db.refresh(pratica)
    
#defining crud for documento

async def get_documento_by_URI(db: AsyncSession, URI: str):
    result = await db.execute(select(Documento).filter(Documento.RedirectURI == URI))
    return result.scalars().first()