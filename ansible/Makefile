.PHONY: all
all:
	ansible-playbook site.yml -vvv

.PHONY: test
test:
	ansible-playbook --syntax-check site.yml

.PHONY: temp
temp:
	ansible-playbook test.yml -vvv
