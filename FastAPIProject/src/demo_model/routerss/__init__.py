from fastapi import APIRouter
from src.demo_model.routerss.item_router import router as item_router

router = APIRouter()

router.include_router(item_router, prefix="/items", tags=["物品"])