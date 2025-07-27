# 02-Containerized-Microservices-Architecture

Here's a clean, beginner-friendly `README.md` for your **multi-container Flask microservice project** using Docker Compose, PostgreSQL, and Redis:

---

### 📘 `README.md`

````markdown
# 🧩 Flask Microservices with Docker Compose

This project demonstrates a simple microservices architecture using Flask, Docker Compose, PostgreSQL, and Redis.

## 📦 Services Overview

| Service       | Description                               | Port     |
|---------------|-------------------------------------------|----------|
| `user-service`| Handles user registration using PostgreSQL| `5000`   |
| `data-service`| Serves user data with Redis caching       | `5001`   |
| `postgres`    | PostgreSQL database for user data         | `5432`   |
| `redis`       | Redis cache for fast data access          | `6379`   |

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

- Docker
- Docker Compose

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/Sayantan2k24/02-Containerized-Microservices-Architecture.git
cd 02-Containerized-Microservices-Architecture
````

### 3️⃣ Run All Services

```bash
docker-compose up --build
```

---

## 🔧 API Endpoints

### ✅ User Registration (user-service)

* **Endpoint**: `POST /register`
* **URL**: `http://localhost:5000/register`
* **Payload**:

```json
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

* **Sample `curl` command**:

```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice", "email":"alice@example.com"}'
```

---

### 📥 Get Cached User Info (data-service)

* **Endpoint**: `GET /user/<name>`

* **URL**: `http://localhost:5001/user/Alice`

* **Behavior**: Returns cached user info if available; else sets it in Redis.

* **Sample `curl` command**:

```bash
curl http://localhost:5001/user/Alice
```

---

## 🗃️ Database Initialization

The `postgres` container loads an initial SQL file from:

```
./init.sql → /docker-entrypoint-initdb.d/init.sql
```

Make sure `init.sql` includes:

```
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
```
OR

TO Limit Size

```sql
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);
```

---

## 🐳 Docker Compose Setup

```yaml
version: '3.8'

services:
  user-service:
    build: ./user-service
    ports:
      - "5000:5000"
    depends_on:
      - postgres
    environment:
      - FLASK_ENV=development
    networks:
      - custom-net

  data-service:
    build: ./data-service
    ports:
      - "5001:5000"
    depends_on:
      - redis
    environment:
      - FLASK_ENV=development
    networks:
      - custom-net

  postgres:
    image: postgres:13
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: users
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - custom-net

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    networks:
      - custom-net

volumes:
  pgdata:

networks:
  custom-net:
    driver: bridge

```

---

## ✅ Verifying Functionality

1. Register a user via `user-service`.
2. Check PostgreSQL to confirm the data is stored.
3. Fetch user via `data-service` to test Redis caching.
4. Confirm second fetch returns a `"cached": true` response.

---

## 📂 Folder Structure

```
.
├── data-service/
│   └── app.py
├── user-service/
│   └── app.py
├── init.sql
├── docker-compose.yml
└── README.md
```

---
