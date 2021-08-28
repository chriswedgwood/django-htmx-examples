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
(venv) $ pip install -r requirements.txt
```

Migrate Database
```bash
(venv) $ python manage.py migrate
```


Run tests
```bash
(venv) $ pytest
```


Run server
```bash
(venv) $ python manage.py runserver
```


