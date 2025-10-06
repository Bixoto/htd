#! /bin/bash -ex
[ ! -f pyproject.toml ] && exit 0

COV_ARGS=""

if [ -n "$HTMLCOV" ]; then
  COV_ARGS="$COV_ARGS --cov-report=html"
fi
if [ -n "$BRANCHCOV" ]; then
  COV_ARGS="$COV_ARGS --cov-branch"
fi

poetry run ruff check htd
poetry run mypy --strict --check-untyped-defs --explicit-package-bases htd/*.py
poetry run pytest --cov=htd $COV_ARGS tests/
