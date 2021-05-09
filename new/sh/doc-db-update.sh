#!/bin/bash
docker exec -d projarka-db sh -c "bash /db/db-update.sh"
echo Please Wait..
docker restart projarka-back
