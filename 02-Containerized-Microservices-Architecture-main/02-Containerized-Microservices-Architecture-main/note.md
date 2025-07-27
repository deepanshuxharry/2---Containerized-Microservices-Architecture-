### ✅ To Manually Test If Everything Is Working

#### 1. **Start All Services**

```bash
docker-compose up --build
```

This will:

* Build and start all services.
* Set up a PostgreSQL DB with a `users` table via `init.sql`.
* Launch Redis, user-service on port `5000`, and data-service on `5001`.

---

### ✅ Test 1: Is `user-service` connected to PostgreSQL?

#### Check logs:

```bash
docker-compose logs user-service
```

#### Register a user:

```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'
```

✅ **Expected Response**:

```json
{"message": "User registered"}
```

#### Enter `postgres` container and verify the data:

```bash
docker exec -it <postgres-container-id-or-name> psql -U postgres -d users
```

Then inside Postgres:

```sql
SELECT * FROM users;
```

---

### ✅ Test 2: Is `data-service` connected to Redis?

#### Example endpoint in `data-service`:

```bash
curl http://localhost:5001/user/Alice
```

✅ **Expected on First Request**:

```json
{
  "name": "Alice",
  "cached": false,
  "info": "User info for Alice"
}
```

✅ **Expected on Second Request**:

```json
{
  "name": "Alice",
  "cached": true,
  "info": "User info for Alice"
}
```

Because Redis is caching the response by name.

---

### ✅ Bonus: Check if Redis is storing keys

Inside the `redis` container:

```bash
docker exec -it <redis-container-id-or-name> redis-cli
```

Then run:

```redis
keys *
get Alice
```

---

### ✅ Summary of Manual Test Commands:

| What                    | Command                                                                                                                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Start services          | `docker-compose up --build`                                                                                                          |
| Register a user         | `curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"name":"Alice", "email":"alice@example.com"}'` |
| Verify DB entry         | `docker exec -it <postgres> psql -U postgres -d users`                                                                               |
| Fetch from data-service | `curl http://localhost:5001/user/Alice`                                                                                              |
| Check Redis keys        | `docker exec -it <redis> redis-cli` then `keys *`                                                                                    |