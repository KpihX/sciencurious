.PHONY: push integration

push:
	@echo "--> Pushing to all remotes (github & gitlab)..."
	git push github HEAD
	git push gitlab HEAD

integration:
	cd math/integration/scripts && uv run integration.py
