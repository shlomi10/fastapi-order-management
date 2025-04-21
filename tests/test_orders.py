import requests
import pytest
import allure
from utils import data_generator

@allure.feature("Order Management")
@allure.story("Create a new order")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create a new order successfully")
def test_create_order(base_url):
    order_data = data_generator.generate_order()
    response = requests.post(f"{base_url}/orders", json=order_data)
    assert response.status_code == 200

    created_order = response.json()
    assert created_order["user_id"] == order_data["user_id"]
    assert created_order["status"] == "Pending"
    assert "_id" in created_order

@allure.feature("Order Management")
@allure.story("Retrieve an order by ID")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Retrieve an order by its ID")
def test_get_order_by_id(base_url):
    order_data = data_generator.generate_order()
    create_response = requests.post(f"{base_url}/orders", json=order_data)
    created_order = create_response.json()

    get_response = requests.get(f"{base_url}/orders/{created_order['_id']}")
    assert get_response.status_code == 200
    retrieved_order = get_response.json()
    assert retrieved_order["user_id"] == order_data["user_id"]
    assert retrieved_order["status"] == "Pending"

@allure.feature("Order Management")
@allure.story("Retrieve all orders")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Retrieve all orders successfully")
def test_get_all_orders(base_url):
    response = requests.get(f"{base_url}/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@allure.feature("Order Management")
@allure.story("Update an order status")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Update an order's status to Shipped")
def test_update_order_status(base_url):
    order_data = data_generator.generate_order()
    create_response = requests.post(f"{base_url}/orders", json=order_data)
    created_order = create_response.json()
    order_id = created_order["_id"]

    update_response = requests.put(f"{base_url}/orders/{order_id}", json={"status": "Shipped"})
    assert update_response.status_code == 200

    get_response = requests.get(f"{base_url}/orders/{order_id}")
    updated_order = get_response.json()
    assert updated_order["status"] == "Shipped"

@allure.feature("Order Management")
@allure.story("Delete an order")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Delete an order successfully")
def test_delete_order(base_url):
    order_data = data_generator.generate_order()
    create_response = requests.post(f"{base_url}/orders", json=order_data)
    created_order = create_response.json()
    order_id = created_order["_id"]

    delete_response = requests.delete(f"{base_url}/orders/{order_id}")
    assert delete_response.status_code == 200

    get_response = requests.get(f"{base_url}/orders/{order_id}")
    assert get_response.status_code == 404

@allure.feature("Order Management")
@allure.story("Update order status - parameterized values")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Update order status to different states")
@pytest.mark.parametrize("new_status", ["Processing", "Shipped", "Delivered"])
def test_update_status_parametrized(base_url, new_status):
    order_data = data_generator.generate_order()
    create_response = requests.post(f"{base_url}/orders", json=order_data)
    created_order = create_response.json()
    order_id = created_order["_id"]

    update_response = requests.put(f"{base_url}/orders/{order_id}", json={"status": new_status})
    assert update_response.status_code == 200

    get_response = requests.get(f"{base_url}/orders/{order_id}")
    updated_order = get_response.json()
    assert updated_order["status"] == new_status

@allure.feature("Order Management - Negative Tests")
@allure.story("Create order with missing fields")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create order with missing fields - expect 422 error")
def test_create_order_with_missing_fields(base_url):
    invalid_order = {
        "total_price": 500,
        "status": "Pending"
    }
    response = requests.post(f"{base_url}/orders", json=invalid_order)
    assert response.status_code == 422  # Unprocessable Entity

@allure.feature("Order Management - Negative Tests")
@allure.story("Update a non-existent order")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Update a non-existent order - expect 404 error")
def test_update_nonexistent_order(base_url):
    fake_id = "000000000000000000000000"
    response = requests.put(f"{base_url}/orders/{fake_id}", json={"status": "Shipped"})
    assert response.status_code == 404


