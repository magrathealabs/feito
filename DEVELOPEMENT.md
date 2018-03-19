# Development Guide

## Dependencies

Install development dependencies:

```bash
pip install -r requirements/development.txt
```

## Tests

```sh
pytest
```

## Releases

### PyPI

Add your credentials from PyPI to `~/.pypirc`:

```
[pypi]
username:<USERNAME>
password:<PASSWORD>
```

To release a new version to PyPI:

```sh
python setup.py sdist
twine upload dist/*
```
