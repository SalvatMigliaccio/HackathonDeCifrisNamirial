from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from  core.config import Settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None, isOperator: bool = False
) -> str:
    expire = datetime.utcnow() + expires_delta if expires_delta else timedelta(
        minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {
        "iat": datetime.utcnow(),
        "exp": expire,
        "sub": str(subject),
        "isOperator":  isOperator
    }
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_PRIVATE_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)