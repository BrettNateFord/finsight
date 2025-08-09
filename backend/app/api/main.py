from fastapi import FastAPI
from app.api.v1.routes import router as api_router
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(settings.FRONTEND_ORIGIN)],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": f"{settings.PROJECT_NAME} backend is running."}
