#!/usr/bin/env bash

set -eu

host=127.0.0.1
port=8000

get_absolute_path() {
  cd "$(dirname "$1")" && pwd -P
}

cd "$(get_absolute_path "$0")" || exit 1

[[ "${HOST:-}" ]] && host="${HOST}"
[[ "${PORT:-}" ]] && port="${PORT}"
poetry run alembic upgrade head
poetry run uvicorn --host "${host}" --port "${port}" --reload src.main:app
