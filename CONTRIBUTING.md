# Contribution guidelines

## Database

Alembic is used to create migrations for the database. The applicable revisions
can be found in `alembic/versions/`.

To create a new migration:

```
$ poetry run alembic revision --autogenerate
```

To initialize a database from scratch or update an existing one to the current
latest migration:

```
$ poetry run alembic upgrade head
```

## Running tests and using helpers with tox

Tox is used to run tests on the application:

```
$ tox
```

For now, the only target that we have is for linting (`linter`).
You can run a specific target like this:

```
$ tox -e <target>
```

## Code formatter

[black](https://black.readthedocs.io/en/stable/) is used to format the code in
this repository, with a linting step checking for it. To run it on your code
invoke it like this:

```
$ poetry run black .
```
