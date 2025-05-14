# Makefile

.PHONY: test unit integration e2e lint

test:  ## Run all tests
	pytest -v tests

unit:  ## Run only unit tests
	pytest -v tests/unit

integration:  ## Run only integration tests
	pytest -v tests/integration

e2e:  ## Run end-to-end tests
	pytest -v tests/e2e

lint:  ## Run linter
	flake8 .
