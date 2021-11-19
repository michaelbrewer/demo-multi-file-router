
update-requirements:
	pipenv lock -r > users/requirements.txt

test:
	pipenv run pytest