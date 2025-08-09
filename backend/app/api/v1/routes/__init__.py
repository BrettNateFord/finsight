# app/api/v1/routes/__init__.py
from fastapi import APIRouter
from . import overview, portfolio, transactions, reports, settings

router = APIRouter()
router.include_router(overview.router, prefix="/overview", tags=["Overview"])
router.include_router(portfolio.router, prefix="/portfolio", tags=["Portfolio"])
router.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
router.include_router(reports.router, prefix="/reports", tags=["Reports"])
router.include_router(settings.router, prefix="/settings", tags=["Settings"])
