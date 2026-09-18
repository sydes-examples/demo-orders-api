from fastapi import FastAPI, HTTPException, status

from app.models import InventoryItem, Order, OrderCreate
from app.service import (
    InsufficientStockError,
    UnknownSkuError,
    create_order as create_order_service,
    get_stock,
)

app = FastAPI(title="Demo Orders API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/inventory/{sku}", response_model=InventoryItem)
def read_inventory(sku: str) -> InventoryItem:
    try:
        stock = get_stock(sku)
    except UnknownSkuError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SKU not found") from exc

    return InventoryItem(sku=sku, stock=stock)


@app.post("/orders", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate) -> Order:
    try:
        return create_order_service(order)
    except UnknownSkuError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SKU not found") from exc
    except InsufficientStockError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient stock") from exc
