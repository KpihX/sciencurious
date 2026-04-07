.PHONY: push

push:
	@echo "--> Pushing to all remotes (github & gitlab)..."
	git push github HEAD
	git push gitlab HEAD
