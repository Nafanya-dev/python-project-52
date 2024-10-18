MANAGE := poetry run python manage.py

.PHONY: install
install:
	@poetry install

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	@poetry run flake8 task_manager

.PHONY: start
start:
	@$(MANAGE) runserver

.PHONY: test
test:
	@$(MANAGE) test

.PHONY: coverage
coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report
	poetry run coverage html
