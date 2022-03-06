#!/bin/bash
docker stop redis
docker pull redis:latest
docker run -d --rm --name test-app-redis redis
