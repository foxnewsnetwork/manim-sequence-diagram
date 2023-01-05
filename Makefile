publish:
	poetry publish --build

install:
	poetry install

dev:
	pip install -e .

example1:
	manim -pql docs/examples.py ClientRaceDatabaseNetwork
