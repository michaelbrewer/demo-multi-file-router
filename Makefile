dev:
	pip3 install -U pip pipenv
	pipenv install --dev
update-requirements:
	pipenv lock -r > users/requirements.txt
test:
	pipenv run pytest