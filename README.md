# Django Rest Framework - Example

## Requirements
```
#Python 2.7.3
Django==1.10.1
djangorestframework
```

## Run Project
```
$ pip install -r requirements.txt
$ python manage.py migrate
$ pip manage.py createsuperuser
$ python manage.py migrate
$ python manage.py runserver
```

## Manage users

Log in with the administrator in:

[127.0.0.1:8000/admin](127.0.0.1:8000/admin)

See results in:

[127.0.0.1:8000/users](127.0.0.1:8000/users)

[127.0.0.1:8000/groups](127.0.0.1:8000/groups)

## Hello world
In the third commit is the example of hello world, go back to it to prove it with:
```
$ git reset --hard HEAD~1
```
