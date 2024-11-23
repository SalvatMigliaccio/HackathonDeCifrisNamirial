from datetime import timedelta
from typing import Any
import logging
import requests

from fastapi import APIRouter, Body, Depends, HTTPException, Request, Response, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import crud, models, schemas
from  endpoints import deps
from  core import security
from  endpoints.deps import add_cookie


from  schemas import UserCreate

ACCESS_TOKEN_EXPIRE_MINUTES = 100
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
router = APIRouter()


@router.post("/login")
async def user_auth(
    response: Response,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(deps.get_db),
):
    #user_fiscal_code, url = await login_today_auth(token, token_signature)
    url = "http://localhost:3000"
   

    response = RedirectResponse(
        url=url,
        status_code=302
    )

    db_user: models.User = await crud.get_user_by_email(
        db=db, email=username)
    is_operator = False
    if db_user is None:
        db_user = await crud.get_operator_by_email(db=db, email = username)
        is_operator = True
        if db_user is None:
            raise HTTPException(
                status_code=404, detail="Incorrect email or password")

    if not security.verify_password(password, db_user.password_hash):
        raise HTTPException(
            status_code=404, detail="Incorrect email or password")

    access_token = security.create_access_token(
        db_user.id,
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES), is_operator
    ) or ""

    add_cookie(response=response, key="token", value=access_token)
    return {'token': access_token}

async def signin(
    response: Response,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    is_operator: bool = Form(...),
    db: Session = Depends(deps.get_db),
):
    if is_operator:
        db_user: models.Operatore = crud.get_operator_by_email(
            db=db, email=email)
        if db_user is not None:
            raise HTTPException(
                status_code=400, detail="User already exists")
        user_in = UserCreate(Username=username,email=email, password=password)
        user = crud.create_operator(db=db, operatori=user_in)
        return user
    else:
        db_user: models.User = crud.get_user_by_email(
            db=db, email=email)
        if db_user is not None:
            raise HTTPException(
                status_code=400, detail="User already exists")

        user_in = UserCreate(Username=username,email=email, password=password)
        user = crud.create_user(db=db, user=user_in)
        return user
