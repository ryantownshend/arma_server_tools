#!/bin/bash

# runs gitlab pipeline tests locally
# make sure you are in the python virtual env and the packages mypy, black, ruff, pytest and markdownlint installed!

set -e

echo "===== running mypy         ====="
poetry run mypy --no-error-summary

echo "===== running ruff         ====="
poetry run ruff .

echo "===== running pytest       ====="
poetry run pytest -qq

echo "===== running markdownlint ====="

`markdownlint .`

echo "===== ALL TESTS PASSED!    ====="

echo '
 _______ _______ ______ ______ _______ _______ _______
|     __|   |   |      |      |    ___|     __|     __|
|__     |   |   |   ---|   ---|    ___|__     |__     |
|_______|_______|______|______|_______|_______|_______|
'