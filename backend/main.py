from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.routing import APIRoute

# from  endpoints.deps import get_db

from endpoints.api import api_router
app = FastAPI()

app.include_router(api_router)

# @app.lifespan("startup")
# async def startup():
#     await db.connect()

# @app.lifespan("shutdown")
# async def shutdown():
#     await db.disconnect()



#add route from backend/endpoints/api.py


# APIRouter = APIRoute(prefix=settings.API_V1_STR)