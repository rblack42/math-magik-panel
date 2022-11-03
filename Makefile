.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: pyinit
pyinit:
	pip install -U pip
	pip install pip-tools

.PHONY: reqs
reqs:
	pip-compile
	pip install -r requirements.txt

.PHONY: provision
provision:
	cd ansible && \
		make

.PHONY: nb
nb:
	cd book && \
		jupyter notebook
