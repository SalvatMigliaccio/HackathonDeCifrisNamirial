from typing import Generator
from jose import jwt
from fastapi import Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from sqlalchemy.orm import Session

import crud, models, schemas
from  core import security
from  core.config import Settings
from  pygres.database import SessionLocal
import datetime

import logging
logger = logging.getLogger(__name__)

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"api/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        payload = jwt.decode(
            token, Settings.JWT_PRIVATE_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError) as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    session = crud.session.get_by_user(db=db, user_id=user.id)
    _check_session(session)
    return user


def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user


def _check_session(
    session: Session
) -> models.User:

    object_name = \
        "Session" if not session else \
        "Self JWT" if not session.self_jwt else \
        "Voting JWT" if not session.voting_jwt else \
        None

    if object_name:
        logger.error(f"{object_name} not found")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"{object_name} not found")

    self_jwt_claims = jwt.get_unverified_claims(session.self_jwt)

    if session.revoked_at:
        if (datetime.datetime.fromisoformat(session.revoked_at) > datetime.datetime.fromtimestamp(self_jwt_claims["iat"])):
            logger.error("Session revoked")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Session revoked")

    # check if self_jwt is still valid
    if (datetime.datetime.fromtimestamp(self_jwt_claims["exp"]) < datetime.datetime.now()):
        logger.error("Session expired")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Session expired")

def add_cookie(response: Response, key, value: str, **kwargs):
    response.set_cookie(key=key,
                        value=value,
                        max_age=Settings.ACCESS_TOKEN_EXPIRE_MINUTES*60,
                        domain=Settings.COOKIES_DOMAIN if Settings.COOKIES_DOMAIN else None,
                        **kwargs
                        )