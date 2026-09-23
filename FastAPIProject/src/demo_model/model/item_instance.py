from typing import Optional

from sqlmodel import SQLModel, Field, create_engine, Session


class ItemData(SQLModel):

        new_id:int
        item_name:str
        item_price:float
        item_description:Optional[str] = None
