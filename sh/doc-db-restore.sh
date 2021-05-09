#!/bin/bash
docker exec -d projarka-db sh -c "mysql -prootdb projarka < db/projarka.sql"
echo Please Wait...
docker restart projarka-back
