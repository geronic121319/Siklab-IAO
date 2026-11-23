# Siklab AI

This repository contains the initial web landing page plus a minimal scaffold for
the Siklab AI incident reporting prototype.

## Django API

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API is available at `http://localhost:8000/api/`. `GET /api/incidents/`
lists incidents and `POST /api/incidents/` creates an incident.

For local test runs that do not require PostgreSQL:

```bash
DB_ENGINE=django.db.backends.sqlite3 POSTGRES_DB=/tmp/siklab.sqlite3 \
  python manage.py test
```

## PostgreSQL

The provided Docker Compose stack starts PostgreSQL and Django:

```bash
docker compose up --build
```

The initial migration enables PostgreSQL row-level security on incidents and
defines dispatcher and reporter policies. The Django database-role middleware
injects `app.current_role` and `app.current_user_id` into each PostgreSQL
session.

## React web client

```bash
cd frontend
npm install
npm run dev
```

Vite proxies `/api` requests to Django on port 8000.

## Android

`mobile/Incident.kt` is a serializable Kotlin data transfer model that matches
the Django incident JSON shape. A Jetpack Compose application can consume this
model through its existing Retrofit/Kotlin Serialization network layer.
