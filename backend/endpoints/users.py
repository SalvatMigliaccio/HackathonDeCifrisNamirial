from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from endpoints.deps import get_db
import crud, models, schemas
from  endpoints import deps
from  core.utils import send_new_account_email
from  core import security


router = APIRouter()


@router.post("/", response_model=schemas.UserBase)
async def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user.
    """
    if await crud.get_user_by_email(db, email=user_in.email):
        
        raise HTTPException(
            status_code=400,
            detail=f"The user with this username already exists in the system.",
        )
    user_in.password_hash = security.hash_password(user_in.password_hash)
    user = await crud.create_user(db, user=user_in)

    return user


@router.put("/me", response_model=schemas.UserBase)
def update_user_me(
    *,
    db: Session = Depends(get_db),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserCreate(**current_user_data)

    if email is not None:
        user_in.email = email

    user = crud.update_user(db, user_in)
    return user


@router.get("/me", response_model=schemas.UserBase)
def read_user_me(
    groups: bool = False,
    dossiers: bool = False,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    if groups and dossiers:
        raise HTTPException(status_code=422, detail="Both groups and dossiers cannot be processed")
    if groups:
        return crud.get_groups(current_user.id)
    if dossiers:
        return crud.get_dossiers(current_user.id)
    return current_user


@router.get("/", response_model=schemas.UserBase)
async def get_user(email: str, db: Session = Depends(get_db)):
    response = crud.get_user_by_email(db, email)
    if not response:
        raise HTTPException(status_code=404)
    return response