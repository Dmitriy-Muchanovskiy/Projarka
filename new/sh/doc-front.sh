#!/bin/bash
docker build --rm -t projarka-front -f front/Dockerfile .
docker run --rm --network=projarka-net --ip=172.20.0.4 -p 3380:80 --name projarka-front -d projarka-front

