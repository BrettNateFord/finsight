from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_settings():
    return {"message": "Settings endpoint working"}
