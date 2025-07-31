# Personal Finance Dashboard

A modern web API for managing and tracking personal income, expenses, and financial goals, built with **FastAPI**. This project is ideal for individuals who want to gain better control of their finances or developers seeking a backend-focused portfolio piece.

---

## Features

-  User registration and login (JWT-based authentication)
-  Track income and expenses by category and date
-  Monthly summaries and budget planning
-  CRUD operations for financial records
-  RESTful API with auto-generated docs (Swagger & Redoc)
-  Deployed-ready structure with environment separation

---

## 🛠 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite (or PostgreSQL ready)
- **ORM**: SQLAlchemy
- **Authentication**: OAuth2 with JWT
- **Others**: Pydantic, Uvicorn, Alembic (optional)

---

## 🗂 Project Structure

app/
│
├── main.py # Entry point
├── models/ # SQLAlchemy models
├── schemas/ # Pydantic data validation
├── routes/ # API route definitions
├── services/ # Business logic
├── database/ # DB connection
└── utils/ # Utility functions (e.g., token generation)

---

##  Installation

```bash
# 1. Clone this repo
git clone https://github.com/your-username/personal-finance-dashboard.git
cd personal-finance-dashboard

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn app.main:app --reload
API Documentation
Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

Example Endpoints
POST /register – Create a new user

POST /login – Authenticate user and receive JWT

POST /incomes/ – Add a new income

POST /expenses/ – Add a new expense

GET /summary/monthly – View monthly budget summary

Author
Arturo Sirlopú
Python Backend Developer
LinkedIn | GitHub

License
MIT License – feel free to fork and use this project for learning or personal use.
