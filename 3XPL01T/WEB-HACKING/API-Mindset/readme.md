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


GET /api/register HTTP/2 <br>
Host: localhost:3000 <br>
User-Agent: <?> <br>
Content-Type: application/json <br>

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


GET /api/login HTTP/2 <br>
Host: localhost:3000 <br>
User-Agent: <?> <br>
Content-Type: application/json <br>

{
  "usernameOrEmail": "user",
  "password": "user123"
}

Success Response: <br>
{
  "message": "success",
  "accessToken": "token"
}


## 📥 GET `/api/users`

PROFILE


GET /api/users HTTP/2 <br>
Host: localhost:3000 <br>
User-Agent: <?> <br>
Content-Type: application/json <br>
Authorization : Bearer  <token> <br>



Success Response: <br>
{
    "_id": "6718ddd33ecefa69806ebf71",
    "username": "user",
    "email": "user@user.com",
    "role": "pejabat",
    "birthday": "1999-03-19",
    "displayName": "noSystemIsSafe",
    "gender": "male"
}

