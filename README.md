# Portfolio project

## Setup

Clone the repository
```sh
$ git clone https://github.com/Susu-spec/django_portfolio.git
$ cd django_portfolio
```

Create and activate a virtual environment (`env` is the virtual environment name)
```sh
$ python3 -m venv env
$ source env/bin/activate
```

Install django
```sh
$ pip install django
```

## Usage

Change to sub-directory
```sh
$ cd Portfolio
```

Create superuser
```sh
$ python manage.py createsuperuser
```

Run development server
```sh
$ python manage.py runserver
```

Navigate to http://127.0.0.1:8000 (django servers are set to port number 8000 by default)

If need for a specific port (`portnumber` is the port you wish to use), run:
```sh
$ python manage.py runserver portnumber
```

