install:
	poetry install

brain-games:
	poetry run brain-games

brain-calc:
	poetry run brain-calc

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games_1

brain-even:
	poetry run brain-even

brain-gcd:
	poetry run brain-gcd

reinstall:
	pip install --user dist/*.whl --force-reinstall


