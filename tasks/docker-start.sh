#!/bin/bash
docker compose --env-file docker/config.env -f docker/docker-compose.yml up -d --build