from app import repository
from app.models import Order, OrderCreate


class UnknownSkuError(ValueError):
    pass


class InsufficientStockError(ValueError):
    pass


def get_stock(sku: str) -> int:
    stock = repository.get_stock(sku)
    if stock is None:
        raise UnknownSkuError(sku)
    return stock


def create_order(order: OrderCreate) -> Order:
    available_stock = get_stock(order.sku)
    if order.quantity > available_stock:
        raise InsufficientStockError(order.sku)

    return repository.save_order(order)
