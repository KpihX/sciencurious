UV := $(shell command -v uv)
PYTHON := $(UV) run python

.PHONY: help push integration sync-cpu sync-xpu sync-cuda kernel smoke

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST)

sync-cpu:
	@$(UV) sync --extra cpu

sync-xpu:
	@$(UV) sync --extra xpu

sync-cuda:
	@$(UV) sync --extra cuda

sync: sync-xpu

kernel: sync 
	@$(PYTHON) -m ipykernel install --user --name=sciencurious --display-name="sciencurious"

push:
	@echo "--> Pushing to all remotes (github & gitlab)..."
	git push github HEAD
	git push gitlab HEAD

integration:
	cd math/integration/scripts && uv run integration.py

smoke: ## Smoke checks (pyproject + lockfile resolution + help)
	@python3 -c "import tomllib; d=tomllib.load(open('pyproject.toml','rb')); u=d['tool']['uv']; assert u['index-strategy']=='unsafe-best-match', u['index-strategy']; assert {e['extra'] for c in u['conflicts'] for e in c}=={'cpu','cuda','xpu'}, u['conflicts']; print('toml ok')"
	@$(UV) lock --check
	@timeout 15 $(MAKE) --no-print-directory help
