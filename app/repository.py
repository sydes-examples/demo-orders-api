from app.models import Order, OrderCreate

_INVENTORY: dict[str, int] = {
    "BOOK-001": 10,
    "MUG-001": 5,
    "PEN-001": 20,
}

_ORDERS: list[Order] = []


def get_stock(sku: str) -> int | None:
    return _INVENTORY.get(sku)


def save_order(order: OrderCreate) -> Order:
    saved_order = Order(id=len(_ORDERS) + 1, sku=order.sku, quantity=order.quantity)
    _ORDERS.append(saved_order)
    return saved_order


def clear_orders() -> None:
    _ORDERS.clear()
