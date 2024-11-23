# from  core.config import Settings
from fastapi import APIRouter

from  endpoints import login, users, utils, groups, dossier

api_router = APIRouter(prefix="/api")
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(groups.router, prefix="/groups", tags=["groups"])
api_router.include_router(dossier.router, prefix="/dossier", tags=["dossier"])