from typing import List

from fastapi import APIRouter
from src.demo_model.DTO.from_item import ItemCreate
from src.demo_model.service.service_fromitem import service_read_items

router = APIRouter()

@router.get("/",response_model=List[ItemCreate],summary="获取物品列表")
def get_items(skip: int = 0, limit: int = 10):

    """
    获取物品列表的API端点

    参数:
        skip (int, optional): 跳过的物品数量，默认为0
        limit (int, optional): 返回的物品数量上限，默认为10

    返回:
        List[ItemCreate]: 物品列表，每个物品都是ItemCreate模型
    """
    lists:list[ItemCreate]  # 声明一个ItemCreate类型的列表变量
    lists = service_read_items(skip, limit)  # 调用服务层方法获取物品列表
    return lists  # 返回获取到的物品列表