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
  poetry run black . -t martynvandijke/soundbridgefx:dev


#
@poetry: poetry_build
  poetry run semantic-release publish

#poetry build
@poetry_build:
  poetry build

@web: web_build

@web_update:
  cd web && npm update

@web_build: web_update
  cd web && npm run build
  cp -r web/.svelte-kit/output/client/ soundbridgefx/web
  cp -r web/.svelte-kit/output/prerendered soundbridgefx/web

# Build docker file
@docker_build:
  docker build .

@docker: docker_build