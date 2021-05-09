#!/bin/bash
docker network create projarka-net --subnet=172.20.0.0/16 
docker build --rm -t projarka-db -f db/Dockerfile .
docker run --rm --network=projarka-net --ip=172.20.0.2 --name projarka-db -d projarka-db
echo Please Wait...
sleep 30
docker exec -d projarka-db sh -c "bash /db/db-create.sh"

