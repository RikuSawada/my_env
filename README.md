# Development Environment

This repository contains a simple full stack sample composed of:

- **backend** – Spring Boot application running on Java 17
- **frontend** – Angular application
- **db** – PostgreSQL 12
- **nginx** – reverse proxy in front of the backend and frontend

Docker Compose is used to run the stack locally.

## Prerequisites

- Docker and Docker Compose V2 installed

## Usage

Build and start all containers:

```bash
docker compose up --build
```

The services can also be started individually. For example, launch the database first and then the backend:

```bash
docker compose up db
# in another terminal
docker compose up backend
```

The frontend depends on the backend and will serve the Angular app on port 4200:

```bash
docker compose up frontend
```

Finally, run the reverse proxy which exposes the whole application on port 80:

```bash
docker compose up nginx
```

Access the application via `http://localhost/`.
