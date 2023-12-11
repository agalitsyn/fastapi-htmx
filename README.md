# FastAPI HTMX

Attempt to implement web application without JS frameworks, like React.

- FastAPI for HTTP server
- SQLAlchemy for defining storage models and building SQL queries.
- Pydantic for defining schemas and validate them, but there is no schemas except config when you use templates.
- Jinja2 for templating.
- TailwindCSS as CSS framework.
- Flowbite + Alpine.js for components library.
- HTMX for communication with backend.

## Setup

```sh
cp .env.template .env
docker compose up postgres

poetry install
make build-static
make run
```

Open `http://127.0.0.1:8080`.

Open `http://localhost:8080/admin` and create first user or use plain sql:

```sh
psql 'postgres://postgres:postgres@localhost:5432/postgres' -C "insert into users (email, full_name, role, hashed_password) values ('admin@foo.bar', 'Admin', 'admin', 'admin');"
```
