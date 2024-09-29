#!/usr/bin/env bash

set -o errexit

poetry install --no-dev

poetry run python manage.py collectstatic --no-input

python run python manage.py migrate