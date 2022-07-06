from fastapi import APIRouter


router = APIRouter(tags=['users'])

@router.get('/check_users')
async def users_page():
    return {
        "message": "Hello user"
    }

