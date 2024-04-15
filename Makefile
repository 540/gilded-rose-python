.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Setup local environment
	@pdm install

.PHONY: test
test:  ## Locally run unit tests
	@pdm run pytest

.PHONY: test-watch
test-watch:  ## Locally run unit tests in watch mode
	@pdm run ptw .

.PHONY: test-cov
test-cov:  ## Locally run unit tests with test coverage
	@pdm run pytest --cov

.PHONY: example
example:  ## Run example
	@pdm run texttest_fixture.py

.PHONY: lint
lint:  ## Lint and fix code
	@PIPENV_VERBOSITY=-1
	@pdm run black --target-version=py312 .
	@pdm run pylint --recursive=y ./src ./tests