# 🧬 Mindset API

**Mindset API** is a simple authentication and user profile system built for educational and development purposes.

---

## 🌐 Base URL

http://localhost:3000


---

## 📌 Endpoints Overview

- `POST /api/register` – Register a new user
- `POST /api/login` – Authenticate user and receive JWT token
- `GET /api/users` – Retrieve user profile (requires token)

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


GET /api/register HTTP/2
Host: localhost:3000
User-Agent: <?>
Content-Type: application/json

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

**Request Body:** {
  "usernameOrEmail": "user",
  "password": "user123"
}

GET /api/login HTTP/2
Host: localhost:3000
User-Agent: <?>
Content-Type: application/json

{
  "usernameOrEmail": "user",
  "password": "user123"
}

Success Response:
{
  "message": "success",
  "accessToken": "token"
}


## 📥 GET `/api/users`

PROFILE

**Request Headers:**
Authorization: Bearer <token> <br>
Content-Type: application/json


GET /api/users HTTP/2
Host: localhost:3000
User-Agent: <?>
Content-Type: application/json <br>
Authorization : Bearer  <token>



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

