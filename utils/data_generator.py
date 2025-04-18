import random

def generate_order():
    return {
        "user_id": f"u{random.randint(10000, 99999)}",
        "items": [
            {"product_id": "p001", "name": "Laptop", "price": 1200, "quantity": 1},
            {"product_id": "p002", "name": "Mouse", "price": 25, "quantity": 2}
        ],
        "total_price": 1250,
        "status": "Pending"
    }
