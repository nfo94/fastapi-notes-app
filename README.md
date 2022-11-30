### FastAPI with Docker and PostgreSQL

This is a simple containerized app with crud operations, using PostgreSQL as relational database.
To run the app:

```bash
$ docker-compose up -d --build
```

To run tests:

```bash
$ docker-compose exec web pytest .
```
