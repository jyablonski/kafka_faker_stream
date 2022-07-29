# -include $(shell curl -ssl -o .jacobs-makefile "https://raw.githubusercontent.com/jyablonski/python_aws/jacob/Makefile"; echo .jacobs-makefile)
# this means use curl to download a file from the internet using ssl and write an output file and call it .jacobs-makefile, and then run it afterwards.


.PHONY: docker-build
docker-build:
	@docker-compose -f docker/docker-compose.yml build

.PHONY: docker-run
docker-run:
	@docker-compose -f docker/docker-compose.yml up

.PHONY: docker-run-d
docker-run2:
	@docker-compose -f docker/docker-compose.yml up -d

.PHONY: docker-down
docker-down:
	@docker-compose -f docker/docker-compose.yml down

.PHONY: test
test:
	@pipenv run pytest -v
