# Makefile for notify-me development

.PHONY: help install install-dev test lint format clean build upload

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install:  ## Install the package
	pip install -e .

install-dev:  ## Install the package with development dependencies
	pip install -e ".[dev]"

test:  ## Run tests
	python -m pytest tests/ -v

test-cov:  ## Run tests with coverage
	python -m pytest tests/ -v --cov=notify_me --cov-report=html --cov-report=term

lint:  ## Run linting
	flake8 src/notify_me tests/
	black --check src/notify_me tests/
	isort --check-only src/notify_me tests/
	mypy src/notify_me

format:  ## Format code
	black src/notify_me tests/
	isort src/notify_me tests/

pre-commit-install:  ## Install pre-commit hooks
	pre-commit install

pre-commit-run:  ## Run pre-commit on all files
	pre-commit run --all-files

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:  ## Build distribution packages
	python -m build

check-dist:  ## Check distribution packages
	twine check dist/*

upload-test:  ## Upload to Test PyPI (requires TestPyPI token)
	twine upload --repository testpypi dist/*

upload:  ## Upload to PyPI (requires PyPI token)
	twine upload dist/*

pypi-setup:  ## Interactive PyPI setup helper
	python scripts/setup_pypi.py

pypi-info:  ## Show PyPI setup information
	@echo "📦 PyPI Publishing Quick Reference:"
	@echo ""
	@echo "🔗 Account Registration:"
	@echo "   PyPI: https://pypi.org/account/register/"
	@echo "   Test PyPI: https://test.pypi.org/account/register/"
	@echo ""
	@echo "🔑 API Token Generation:"
	@echo "   PyPI: https://pypi.org/manage/account/token/"
	@echo "   Test PyPI: https://test.pypi.org/manage/account/token/"
	@echo ""
	@echo "🚀 Publishing Commands:"
	@echo "   make pypi-setup     # Interactive setup helper"
	@echo "   make build          # Build distribution packages"
	@echo "   make check-dist     # Validate packages"
	@echo "   make upload-test    # Test on TestPyPI"
	@echo "   make upload         # Publish to PyPI"
	@echo ""
	@echo "📖 Full guide: See PYPI_PUBLISHING.md"

setup-bot:  ## Run interactive bot setup
	notifyme setup

demo:  ## Run a demo command
	notifyme -m "Demo notification from Makefile" echo "Hello, World!"