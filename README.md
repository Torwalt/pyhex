# Python hexagonal architecture

This is my attempt of building a service in a hexagonal (ports & adapters,
onion architecture) pattern. The basic idea is to split the domain (business)
logic from the concrete technical implementations. The domain does not care
about through which means users interact with it (e.g., http, grpc, etc) and the
domain also does not care about the implementation details of specific use
cases (e.g., persistence). Through this approach, services can be developed
that are easy to test, maintain and extend.

## Structure

The service is split into domain, ports and adapters

1. domain: core domain logic, decoupled from API network protocol and persistence solution.
2. ports: implementation of domain usecases, e.g. persistence logic
3. adapters: access points into domain, e.g. http REST interface

Tests are split into unit and integration tests. The http endpoint tests are kinda inbetween.

## Dev Setup

```bash
# or different venv tool
pyenv virtualenv 3.9.5 hlp
# if you dont have python 3.9.5 installed:
# pyenv install 3.9.5 (can take some time)
pyenv activate hlp

# install all deps
poetry install

# install pre-commit hooks
pre-commit install
```

## Running service

```bash
cp example.env .env
# fill out .env
docker-compose up --build -d
# with venv activated
./start_app.sh
```


