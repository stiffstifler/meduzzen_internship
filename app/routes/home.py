from fastapi import APIRouter
from app.services.test_service import get_test_something

router = APIRouter(tags=['home'])

@router.get('/')
async def home_page():
    return {
        "message": "Hello pal"
    }

@router.get('/test')
async def test_page(id: int):
    return await get_test_something(id)
    
