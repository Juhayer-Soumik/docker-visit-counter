# Docker Visit Counter

A small Flask app that counts page visits, storing the count in Redis. Runs with Docker Compose.

## Run it
    docker compose up --build

Then open http://localhost:5000 and refresh to watch the counter increase. The count persists across restarts thanks to a Docker volume.

## Stack
- Python / Flask
- Redis
- Docker and Docker Compose
