from app import repository
from app.models import Order, OrderCreate


class UnknownSkuError(ValueError):
    pass


def get_stock(sku: str) -> int:
    stock = repository.get_stock(sku)
    if stock is None:
        raise UnknownSkuError(sku)
    return stock


def create_order(order: OrderCreate) -> Order:
    get_stock(order.sku)
    return repository.save_order(order)
