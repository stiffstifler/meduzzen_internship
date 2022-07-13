from fastapi import APIRouter
from app.services.test_service import get_test_something
from app.models.schemas import User
from app.models.schemas import SignUp

router = APIRouter(tags=['home'])

@router.get('/')
async def home_page():
    return {
        "message": "Hello pal"
    }

@router.get('/test')
async def test_page(id: int):
    return await get_test_something(id)



@router.get('/SignUp')
    def SignUp(email: str, password: str)
    return {email: str, password: str}
