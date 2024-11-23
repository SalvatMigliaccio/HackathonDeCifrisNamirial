from fastapi import APIRouter, Depends
from crud import get_group_by_id
from endpoints.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/groups/{id}")
async def get_group(id: int, db: Session = Depends(get_db)):
    response = await get_group_by_id(db, id)
    return response