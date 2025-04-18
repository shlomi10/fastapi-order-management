from pymongo import MongoClient
from dotenv import load_dotenv
import os

# This file is to confirm DB changes and to make the DB operations

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
orders_collection = db["orders"]

def get_order_by_id(order_id):
    return orders_collection.find_one({"_id": order_id})

def delete_order_by_id(order_id):
    return orders_collection.delete_one({"_id": order_id})

def clear_orders_collection():
    return orders_collection.delete_many({})

def order_exists(order_id):
    return orders_collection.find_one({"_id": order_id}) is not None

def update_order_status(order_id, status):
    return orders_collection.update_one(
        {"_id": order_id},
        {"$set": {"status": status}}
    )

