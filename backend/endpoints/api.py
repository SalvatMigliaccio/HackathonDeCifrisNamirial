from backend.core.config import settings
from fastapi import APIRouter

from backend.endpoints import login, users, utils

api_router = APIRouter(prefix=settings.API_V1_STR)
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])