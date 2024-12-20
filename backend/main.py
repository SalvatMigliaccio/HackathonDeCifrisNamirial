from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware


# from  endpoints.deps import get_db

from endpoints.api import api_router
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:8001"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

# @app.lifespan("startup")
# async def startup():
#     await db.connect()

# @app.lifespan("shutdown")
# async def shutdown():
#     await db.disconnect()



#add route from backend/endpoints/api.py


# APIRouter = APIRoute(prefix=settings.API_V1_STR)