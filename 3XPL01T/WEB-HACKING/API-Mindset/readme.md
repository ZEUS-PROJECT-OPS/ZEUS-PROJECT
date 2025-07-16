# 🧬 Mindset API

**Mindset API** is a simple authentication and user profile system built for educational and development purposes.

---

## 🌐 Base URL

http://localhost:3000


---

## 📌 Endpoints Overview

- `POST /api/register` – Register a new user
- `POST /api/login` – Authenticate user and receive JWT token
- `GET /api/getProfile` – Retrieve user profile (requires token)

---

## 📥 POST `/api/register`

Registers a new user.

**Request Headers:**
Content-Type: application/json


**Request Body:**

{
  "username": "user",
  "email": "user@user.com",
  "password": "user123"
}


Success Response:
{
  "message": "User registered successfully"
}


## 📥 POST `/api/login`

LOGIN

**Request Headers:**
Content-Type: application/json

**Request Body:**

{
  "usernameOrEmail": "user",
  "password": "user123"
}


Success Response:
{
  "message": "success",
  "accessToken": "token"
}


## 📥 GET `/api/getProfile`

PROFILE

**Request Headers:**
Authorization: Bearer <token>
Content-Type: application/json


Success Response:
{
    "_id": "6718ddd33ecefa69806ebf71",
    "username": "user",
    "email": "user@user.com",
    "role": "pejabat",
    "birthday": "1999-03-19",
    "displayName": "noSystemIsSafe",
    "gender": "male"
}

