from fastapi import APIRouter
from app.services.test_service import get_test_something
from app.models.schemas import User
from app.models.schemas import SignUp
from app.models.schemas import SignIn
from pydantic import EmailStr

router = APIRouter(tags=['home'])

@router.get('/')
async def home_page():
    return {
        "message": "Hello pal"
    }

@router.get('/test')
async def test_page(id: int):
    return await get_test_something(id)

# db + validator

@router.get('/SignUp')
def SignUp(f_name: str, l_name: str, age: int, city: str, email: EmailStr, password: str):
    return {f_name, l_name, age, city, email, password}

@router.get('/User')
def User(f_name: str, l_name: str, age: int, city: str):
    return {f_name, l_name, age, city}

@router.get('/SignIn')
def User(email: EmailStr, password: str):
    return {email, password}