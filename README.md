# cookiecutter-serious-pycli

[![Build Status](https://travis-ci.org/yanqd0/cookiecutter-serious-pycli.svg?branch=master)](https://travis-ci.org/yanqd0/cookiecutter-serious-pycli)
[![Code style: yapf](https://img.shields.io/badge/code%20style-yapf-blue)](https://github.com/google/yapf)

A python CLI template with `setup.py`, [pytest] and many pytest plugins.

Now, it supports:

- Unit test
- Integration test
- Coverage report for each test above
- Linters
    - pep8
    - flake8
    - pylint
    - yapf
    - isort

Other features:

- A CLI entry
- An auto generated version with `git tag`
- Source code is under `src`, while test code is under `tests` (See [Packaging a python library])

[Packaging a python library]:https://blog.ionelmc.ro/2014/05/25/python-packaging/

[pytest]:https://pytest.org/

## Philosophy

Most people say, Python is not suitable for a big project.

I don't agree with that.

For one thing, most projects are not a real big project, with millions of code.
For another, most Python developers are junior, compared with some other languages like Java.
They are focusing on functions, while making their growing project to a mass of shit.
In some cases, a growing Python project is a growing single file.

I start this project to prove that Python can also construct a serious maintainable project.

A serious python project should start and keep a 100% coverage, at least for unit tests.
Compilation can prevent syntax or other low level issues, while Python don't have it.
So without 100% test coverage, you may be suffered.
Besides, with various linters, the maintainity will be good enough.

Of course, there will be some costs in your development efficiency.
But you can trade it with maintainity freely:
Deliver functions without tests, than make up afterwards, with a good project structure.

After some time, you can fly again.
You will be used to TDD, and the guide of linters.
When you are experienced, the cost will be less and less.

## Requirements

Install `cookiecutter` command line:

```sh
pip install cookiecutter
```

## Usage

Generate a new CookieCutter template layout:

```sh
cookiecutter gh:yanqd0/cookiecutter-serious-pycli
# or
cookiecutter https://github.com/yanqd0/cookiecutter-serious-pycli.git
```

After the project is generated, setup the development environment like that:

```sh
cd demo-project
git init
git add .
git cm -m 'Initialize the project with cookiecutter-serious-pycli'

virtualenv -p python3 .env
. .env/bin/activate
pip install -e .[dev]
```

Now, you can develop and run tests.

## Tests

```sh
pytest
# or
./setup.py test
```

### Unit Test

```sh
pytest --no-pylint -m unit
```

A unit test is for a function or class method.

### Integration Test

```sh
pytest --no-pylint -m integration
```

An integration test is for a module or interface.

Besides, for some reasons, pylint will always run without `--no-pylint`.

### All Without Coverage

Sometimes, test results with and without coverage are different.
Then this will help.

```sh
pytest --no-cov
```

Any linter can be executed independently, like `pylint`:

```sh
pytest -m pylint --no-cov
```
