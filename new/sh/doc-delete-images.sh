#!bash/bin
docker rmi -f projarka-db
docker rmi -f projarka-back
docker rmi -f projarka-front
docker network rm projarka-net
