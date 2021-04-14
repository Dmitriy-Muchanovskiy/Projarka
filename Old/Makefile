export DEPLOY_DATE=$(shell date '+%Y.%m.%d-%H:%M')
define HELP_MESSAGE
Usage: 
	make [command] 
Commands:
	help
	deploy
	update
	restore
	delete_containers
	delete_images 
endef 

export HELP_MESSAGE 

help:
	@echo "$${HELP_MESSAGE}" 

deploy:
	@echo "------- Start deploy -------"
	@echo "Hello Everebody!!"
	@echo "Please wait"
	@bash "sh/doc-net-image-cont-db_create.sh"
	@bash "sh/doc-back.sh"
	@bash "sh/doc-front.sh"
	@echo "Deploying Finished"


front:
	@echo "------- Start front  -------"
	@bash sh/doc-front.sh
	@echo "front of database table is finished"


update:
	@echo "------- Start update DB  -------"
	@bash sh/doc-db-update.sh
	@echo "Changing of database table is finished"

restore:
	@echo "------- Start restore DB -------"
	@bash sh/doc-db-restore.sh
	@echo "Restoring of database table is finished"

delete_containers:
	@echo "------- Start deleting containers -------"
	@bash sh/doc-delete-cont.sh
	@echo "Deleting of containers is finished"

delete_images:
	@echo "------- Start deleting images -------"
	@bash sh/doc-delete-images.sh
	@echo "Deleting of images is finished"
