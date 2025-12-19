# Fitness Tracker Backend
A Django REST API for tracking workouts, nutrition, water intake, and run/walk sessions.
- Django 5.0
- Django REST Framework
- PostgreSQL (via psycopg2-binary)
## Setup
1. Clone the repo:
   git clone https://github.com/Naledi84/fitness-tracker-backend.git
2. Create virtual environment:
   python -m venv venv
   source venv/Scripts/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Start server:
   python manage.py runserver
## API Endpoints
- POST /api/register → Register new user
- POST /api/login → Authenticate user
- GET /api/workouts → List workouts
- POST /api/workouts → Create workout
- GET /api/workouts/<id> → Retrieve workout
- PUT /api/workouts/<id> → Update workout
- DELETE /api/workouts/<id> → Delete workout
##  Next step
- Add Nutrition, Water, Run/Walk endpoints
- Implement JWT authentication
- Write unit tests
## Current Progress
- Custom User model implemented
- JWT authentication (register/login)
- Workout endpoints (CRUD)
- Server running successfully

## How to Test
1. Register a user via `/api/register/`
2. Login via `/api/login/` to get JWT token
3. Use token with `Authorization: Bearer <token>` to access `/api/workouts/`

# Fitness Tracker Backend
A Django REST API for tracking workouts, nutrition, water intake, and run/walk sessions.  
Built with Django 5.0, Django REST Framework, and JWT authentication.
## Tech Stack
- Python 3.14
- Django 5.0
- Django REST Framework
- PostgreSQL (via psycopg2-binary)
- JWT Authentication (djangorestframework-simplejwt)
## Setup
1. Clone the repo:
   git clone https://github.com/Naledi84/fitness-tracker-backend.git
   cd fitness-tracker-backend

2. Create virtual environment:
   python -m venv venv
   source venv/Scripts/activate   # On Windows Git Bash

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Start server:
   python manage.py runserver
## API Endpoints

### Authentication
- POST /api/register → Register new user
- POST /api/login → Obtain JWT token
- POST /api/token/refresh → Refresh JWT token

### Workouts
- GET /api/workouts/ → List workouts (only for logged-in user)
- POST /api/workouts/ → Create workout (auto-linked to logged-in user)
- GET /api/workouts/<id>/ → Retrieve workout
- PUT /api/workouts/<id>/ → Update workout
- DELETE /api/workouts/<id>/ → Delete workout
## Next Steps
- Add Nutrition, Water, and Run/Walk endpoints
- Write unit tests
- Expand documentation

# Fitness Tracker Backend

## 📌 Project Overview
The Fitness Tracker Backend is a Django REST API that helps users track their workouts and monitor fitness progress.  
It allows registration, login with JWT authentication, workout CRUD operations, and provides activity metrics (totals, weekly, and daily breakdowns).

This project was built during the ALX BE Capstone phase (Dec 2025 – Jan 2026).

---

## 🚀 Features
- **User Registration & Login** (JWT authentication)
- **Workout Management** (create, list, update, delete workouts)
- **Activity Metrics**:
  - Totals (duration, calories)
  - Weekly breakdown
  - Daily breakdown

---

## 🛠️ Tech Stack
- **Backend Framework:** Django, Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite (default, can be swapped for PostgreSQL/MySQL)
- **Other Tools:** CORS Headers, Python 3.10+

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/fitness-tracker-backend.git
cd fitness-tracker-backend


