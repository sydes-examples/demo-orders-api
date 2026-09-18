from fastapi.testclient import TestClient

from app.main import app
from app.repository import clear_orders

client = TestClient(app)


def setup_function() -> None:
    clear_orders()


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_inventory_lookup_returns_stock() -> None:
    response = client.get("/inventory/BOOK-001")

    assert response.status_code == 200
    assert response.json() == {"sku": "BOOK-001", "stock": 10}


def test_unknown_sku_returns_404() -> None:
    response = client.get("/inventory/UNKNOWN")

    assert response.status_code == 404


def test_valid_order_creation_returns_201() -> None:
    response = client.post("/orders", json={"sku": "BOOK-001", "quantity": 3})

    assert response.status_code == 201


def test_created_order_contains_expected_sku_and_quantity() -> None:
    response = client.post("/orders", json={"sku": "BOOK-001", "quantity": 3})

    assert response.json()["sku"] == "BOOK-001"
    assert response.json()["quantity"] == 3


def test_rejects_order_when_quantity_exceeds_stock() -> None:
    response = client.post("/orders", json={"sku": "MUG-001", "quantity": 100})

    assert response.status_code == 400
    assert response.json() == {"detail": "Insufficient stock"}


def test_non_positive_quantity_is_rejected() -> None:
    response = client.post("/orders", json={"sku": "BOOK-001", "quantity": 0})

    assert response.status_code == 422
