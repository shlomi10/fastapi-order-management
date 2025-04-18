import os

import pytest
from dotenv import load_dotenv
from pymongo import MongoClient
from utils import db_helper

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Base URL for the API
@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:8000"

# DB fixture (optional if you already use db_helper directly)
@pytest.fixture(scope="session")
def db():
    client = MongoClient(MONGO_URI) # create connection to Mongo
    db = client[DB_NAME] # connect to the DB
    yield db # get the DB for all tests
    client.close()

# Auto-clean orders collection before every test
@pytest.fixture(autouse=True)
def clean_orders_collection():
    db_helper.clear_orders_collection()
