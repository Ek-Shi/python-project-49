lint:
	uv run ruff check brain_games

build:
	uv build

package-install:
	uv tool install --reinstall dist/*.whl

brain-games:
	uv run brain-games

install:
	uv sync	


