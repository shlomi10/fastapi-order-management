import os

import pytest
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Base URL for the API
@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:8000"