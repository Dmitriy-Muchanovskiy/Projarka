#!/bin/bash
docker build --rm -t projarka-back -f back/Dockerfile .
docker run --rm --network=projarka-net --ip=172.20.0.3 -p 8888:8888 --name projarka-back -d projarka-back
