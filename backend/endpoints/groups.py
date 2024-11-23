from fastapi import APIRouter, Depends
from schemas import GruppiBase
from crud import get_group_by_id, create_group
from endpoints.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def create_group(group: GruppiBase, db: Session = Depends(get_db)):
    response = await create_group(db, **group)
    return response

@router.get("/{id}")
async def get_group(id: int, db: Session = Depends(get_db)):
    response = await get_group_by_id(db, id)
    return response