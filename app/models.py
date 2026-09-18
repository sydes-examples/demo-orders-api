from pydantic import BaseModel, Field


class InventoryItem(BaseModel):
    sku: str
    stock: int


class OrderCreate(BaseModel):
    sku: str
    quantity: int = Field(gt=0)


class Order(OrderCreate):
    id: int
