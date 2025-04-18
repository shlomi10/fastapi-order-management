import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List
from datetime import datetime

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

app = FastAPI()

# MongoDB connection
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]  # Database name
orders_collection = db["orders"]  # Collection name


# Pydantic models
class Item(BaseModel):
    product_id: str
    name: str
    price: float
    quantity: int


class Order(BaseModel):
    _id: ObjectId
    user_id: str
    items: List[Item]
    total_price: float
    status: str = "Pending"


class UpdateOrderStatus(BaseModel):
    status: str


# Helper to format MongoDB documents
def order_helper(order) -> dict:
    return {
        "_id": str(order["_id"]),
        "user_id": order["user_id"],
        "items": order["items"],
        "total_price": order["total_price"],
        "status": order["status"],
        "created_at": order["created_at"],
        "updated_at": order["updated_at"]
    }


# Create a new order
@app.post("/orders")
async def create_order(order: Order):
    order_dict = order.dict()
    now = datetime.utcnow()
    order_dict["created_at"] = now
    order_dict["updated_at"] = now
    result = await orders_collection.insert_one(order_dict)
    new_order = await orders_collection.find_one({"_id": result.inserted_id})
    return order_helper(new_order)


# Get a single order by ID
@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    try:
        obj_id = ObjectId(order_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid order ID format")

    order = await orders_collection.find_one({"_id": obj_id})
    if order:
        return order_helper(order)
    raise HTTPException(status_code=404, detail="Order not found")


# Get all orders
@app.get("/orders")
async def get_all_orders():
    orders = []
    async for order in orders_collection.find():
        orders.append(order_helper(order))
    return orders


# Update an order status
@app.put("/orders/{order_id}")
async def update_order(order_id: str, order_update: UpdateOrderStatus):
    try:
        obj_id = ObjectId(order_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid order ID format")

    result = await orders_collection.update_one(
        {"_id": obj_id},
        {"$set": {"status": order_update.status, "updated_at": datetime.utcnow()}}
    )
    if result.modified_count == 1:
        updated_order = await orders_collection.find_one({"_id": obj_id})
        return order_helper(updated_order)
    raise HTTPException(status_code=404, detail="Order not found")


# Delete an order
@app.delete("/orders/{order_id}")
async def delete_order(order_id: str):
    try:
        obj_id = ObjectId(order_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid order ID format")

    result = await orders_collection.delete_one({"_id": obj_id})
    if result.deleted_count == 1:
        return {"message": "Order deleted successfully"}
    raise HTTPException(status_code=404, detail="Order not found")
