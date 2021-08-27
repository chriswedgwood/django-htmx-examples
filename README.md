# django-htmx-examples

An app for demonstrating the HTMX examples on https://htmx.org/examples/.
Im am adding one at a time

## Setup

Create a virtual environment.

```bash
$ python3 -m venv venv
```

Activate the virtual environment.

```bash
$ source venv/bin/activate
```

Install developer and application packages.

```bash
$ pip install -r requirements-dev.txt
$ pip install -r requirements.txt
```

```bash
$ python manage.py migrate
```

```bash
$ python manage.py runserver
```


