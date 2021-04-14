export DEPLOY_DATE=$(shell date '+%Y.%m.%d-%H:%M')
define HELP_MESSAGE
Usage: 
	make [command] 
Commands:
	help
	deploy
	migrate
	upgrade
	downgrade
	stop
endef 

export HELP_MESSAGE 

help:
	@echo "$${HELP_MESSAGE}" 

deploy:
	@echo "------- Start deploy -------"
	@echo "Hello Everebody!!"
	@echo "Please wait"
	database
	backend
	frontend
	@echo "Deploying Finished"


migrate:
	@echo "------- Start init DB   -------"
	@docker exec -d projarka-back sh -c "python3 migrate.py db init"
	@echo "Stage of DB init successful"
	@echo "------- Start migrate -------------"
	@docker exec -d projarka-back sh -c "python3 migrate.py db migrate"
	@echo Stage of DB migrate finished

upgrade:
	@echo "------- Start BD update  -------"
	@docker exec -d projarka-back sh -c "python3 migrate.py db upgrade"
	@echo "Updating of DB is finished"

downgrade:
	@echo "------- Start BD downgrade -------"
	@docker exec -d projarka-back sh -c "python3 migrate.py db downgrade"
	@echo "Deleting of containers is finished"

stop:
	@echo "------- Stop Docker and delete -------"
	@echo "Stop Docker-compose and delete images"
	@docker-compose down
	@docker rmi -f docker_back
	@echo "Stoping and deleting is finished"

database:
	@docker-compose up -d db
	@bash "docker/db/sleep.sh"
	@docker exec -d projarka-db sh -c "bash /db/db-create.sh"

backend:
	@docker-compose up -d back

frontend:
	@docker-compose up -d front
