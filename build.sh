#!/usr/bin/env bash

set -o errexit

poetry install

poetry run python manage.py collectstatic --no-input

poetry run python manage.py migrate
