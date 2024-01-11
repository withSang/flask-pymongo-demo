# Flask demo project with MongoDB

## Prerequisites

1. Local Development

- Python 3.11 with dependencies in `requirements.txt`
- MongoDB 6.0.0+

2. Docker Deployment

- Docker 20+ with docker-compose

## Deploy with Docker
1. Execute the command in the command line.
  ```bash
  $ docker compose -f deploy/docker-compose.yml --env-file=.env up --build -d
  ```
