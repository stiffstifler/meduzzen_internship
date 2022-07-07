from fastapi import APIRouter
from fastapi import FastAPI
from app.db import database, User


router = APIRouter(tags=['users'])
app = FastAPI(title="FastAPI and Docker")

@router.get('/check_users')
async def users_page():
    return {
        "message": "Hello user"
    }

@app.get("/")
async def read_root():
    return await User.objects.all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()