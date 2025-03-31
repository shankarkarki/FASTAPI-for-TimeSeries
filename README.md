# Working with FASTAPI and TimeSeries DB
Building an Analytics API service using Python, FastAPI, and Time-series PostgreSQL with TimescaleDB.

## Prerequisites
- Docker
- Docker Compose
- Python 3.x
- PostgreSQL (TimescaleDB)


## Setup & Usage

### Build and Run with Docker
```sh
docker build -t analytics-api -f Dockerfile.web .
docker run analytics-api
```

### Using Docker Compose
```sh
docker compose up --watch
```
To stop and remove containers:
```sh
docker compose down
```
To stop and remove containers with volumes:
```sh
docker compose down -v
```

### Running Commands in the Container
To access the container shell:
```sh
docker compose run app /bin/bash
```
To run Python inside the container:
```sh
docker compose run app python

