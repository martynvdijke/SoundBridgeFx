# Run tests and linters
@default: poetry

# Setup project
@init:
  pip install poetry
  poetry install

# Run pytest with supplied options
@test *options:
  poetry run pytest {{options}}

# Run linters: black, flake8, mypy, cog
@lint:
  poetryrun black . --check
  poetry run flake8
  poetry run mypy

# Apply Black
@black:
  poetry run black .

# Build docker file
@docker_build:
  docker build .

#
@poetry: poetry_build
  poetry run semantic-release publish


#poetry build
@poetry_build:
  poetry build
