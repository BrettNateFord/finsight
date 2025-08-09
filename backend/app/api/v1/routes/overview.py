from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_overview():
    return {"message": "Overview endpoint working"}
