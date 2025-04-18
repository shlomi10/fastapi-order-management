# 🚀 FastAPI Order Management System

<div align="center">

**[Python 3.12](https://www.python.org/)** &nbsp;|&nbsp;
**[FastAPI 0.110](https://fastapi.tiangolo.com/)** &nbsp;|&nbsp;
**[MongoDB 6.0](https://www.mongodb.com/)** &nbsp;|&nbsp;
**[Docker Compose](https://docs.docker.com/compose/)**

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green.svg?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0-green.svg?style=for-the-badge&logo=mongodb)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg?style=for-the-badge&logo=docker)](https://docs.docker.com/compose/)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/shlomi10/fastapi-order-management/ci.yml?branch=main&label=CI%20Build&style=for-the-badge&logo=github-actions)](https://github.com/shlomi10/fastapi-order-management/actions)
[![Allure Report](https://img.shields.io/badge/Allure-Report-orange.svg?style=for-the-badge&logo=junit5)](https://docs.qameta.io/allure/)

</div>

## 📚 Project Overview

This project is a **simple Order Management System (OMS)** built with:

- **FastAPI** (Python 3.12)
- **MongoDB** (database for orders)
- **Docker & Docker Compose** (for environment setup)
- **GitHub Actions** (for CI/CD pipeline)
- **Allure Reports** (for automated test reporting)

### Key Features

✅ **Create new orders**  
✅ **Retrieve orders**  
✅ **Update order statuses**  
✅ **Delete orders**  
✅ **Run full API tests with Allure reports**

## 🛠️ Installation & Setup

### Prerequisites

- **Git**
- **Docker and Docker Compose**
- *(Optional)* **Python 3.12** for local development

### Step 1: Clone the Repository

```bash
git clone https://github.com/shlomi10/fastapi-order-management.git
cd fastapi-order-management
```

### Step 2: Install Docker and Docker Compose

If Docker is not installed:

1. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Verify installation:

```bash
docker --version
docker-compose --version
```

### Step 3: (Optional) Setup Python Environment for Local Development

If you prefer running without Docker:

1. Install Python 3.12
2. Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install allure-pytest
```

### Step 4: Create Environment Configuration

At the root of the project, create a `.env` file:

```
MONGO_URI=mongodb://mongo:27017
DB_NAME=ecommerce
```

### Step 5: Build and Run with Docker Compose

```bash
docker-compose up --build
```

This will:
- **Build the FastAPI application**
- **Start the MongoDB service**
- **Connect them via Docker network**

### Step 6: Access the Application

Once running, open the Swagger UI:

```
http://localhost:8000/docs
```

## 🧪 Testing

### Running Tests and Generating Reports

1. Run the API tests:

```bash
pytest tests/ --alluredir=allure-results
```

2. Serve the Allure Report:

```bash
allure serve allure-results
```

## 📦 API Endpoints

| Method | URL | Description |
|:------:|-----|-------------|
| **POST** | `/orders` | **Create a new order** |
| **GET** | `/orders/{order_id}` | **Get an order by ID** |
| **GET** | `/orders` | **List all orders** |
| **PUT** | `/orders/{order_id}` | **Update an order's status** |
| **DELETE** | `/orders/{order_id}` | **Delete an order** |

## 🛡️ Continuous Integration (CI/CD)

Every push to the main branch triggers GitHub Actions to:

- **Start MongoDB service**
- **Install dependencies**
- **Run tests**
- **Collect and upload Allure reports**

**[View GitHub Actions](https://github.com/shlomi10/fastapi-order-management/actions)**

## 🗺️ Architecture Diagram

```
+------------------------+
|    User (Client)       |
+----------+-------------+
           |
           v
+----------+-------------+
|    FastAPI App         |
|  (Docker Container)    |
+----------+-------------+
           |
           v
+----------+-------------+
|      MongoDB           |
|  (Docker Container)    |
+------------------------+
```

## 📄 License

**MIT License**

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 🙌 How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
3. **Commit your changes**
4. **Open a pull request**

**Contributions are welcome!**

## 📋 Quick Reference

| Action | Command |
|--------|---------|
| **Clone the repo** | `git clone https://github.com/shlomi10/fastapi-order-management.git` |
| **Create virtual environment** | `python -m venv venv` |
| **Activate environment (Windows)** | `venv\Scripts\activate` |
| **Activate environment (Linux/Mac)** | `source venv/bin/activate` |
| **Install dependencies** | `pip install -r requirements.txt` |
| **Start all services** | `docker-compose up --build` |
| **Stop services** | `docker-compose down` |
| **Run tests** | `pytest tests/ --alluredir=allure-results` |
| **Serve Allure report** | `allure serve allure-results` |

---

<div align="center">

## 👏 Thank you for checking out this project!

**Happy coding! 🚀**

</div>