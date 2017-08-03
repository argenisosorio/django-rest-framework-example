# Django Rest Framework - ModelSerializer

In this example, we record a TV series with the fields (name, release_date, rating, category)
from the django admin, and show the list of series in json format.

## Requirements
```
Python 2.7.3
Django==1.10.1
djangorestframework
```

## Run Project
```
$ pip install -r requirements.txt
$ python manage.py makemigrations series
$ python manage.py migrate
$ pip manage.py createsuperuser
$ python manage.py migrate
$ python manage.py runserver
```
