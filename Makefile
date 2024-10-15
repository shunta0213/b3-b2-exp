MAKEFILE_DIR := $(dir $(lastword $(MAKEFILE_LIST)))

.PHONY: set-env
set-env:
	@tlmgr conf texmf $(KEY) $(VALUE)
	@echo '\CatchFileEdef{\\var$(KEY)}{|"kpsewhich -var-value=$(KEY)"}{\\endlinechar=-1 }' >> ./src/styles/env.sty

.PHONY: venv
venv:
	@python3 -m venv venv

.PHONY: clean
clean:
	@find . -type f -name "*.bak*" -exec rm {} +
	@find . -type f -name "indent.log" -exec rm {} +

.PHONY: prod
prod:
	@echo "Building production version..."
	@grep -q '\\usepackage{src/styles/draft}' main.tex && \
		echo "\033[31mWARNING: The document is using the draft style package.\033[0m" || \
		echo "No draft style package found."
	@latexmk -pdf -silent -outdir=./build
ifneq ($(NAME),)
	@mv ./build/main.pdf ./build/$(NAME).pdf
endif
