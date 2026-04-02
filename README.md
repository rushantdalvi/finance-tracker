# Finance Tracker Backend (FastAPI)

## Overview
This project is a Python-based backend system for managing personal finance records.
It allows users to track income and expenses, view summaries, and perform CRUD operations.

## Features
- Create, Read, Delete transactions
- Financial summary (income, expense, balance)
- SQLite database
- Clean modular structure

## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy

## Setup Instructions
1. Clone repo
2. Install dependencies:
   pip install fastapi uvicorn sqlalchemy pydantic passlib[bcrypt]

3. Run server:
   python -m uvicorn main:app --reload
   

4. Open API docs:
   http://127.0.0.1:8000/docs

## API Endpoints
- POST /transactions
- GET /transactions
- DELETE /transactions/{id}
- GET /summary

## Assumptions
- Dummy user used instead of full authentication
- Roles simplified

## Future Improvements
- JWT Authentication
- Role-based access
- Filtering & pagination
- Unit tests


