# Welcome to the phrases django app

## Purpose of this project

This is a project to learn about django.
This is a code based on linkedin learning course: [Django Essential Training](https://www.linkedin.com/learning/django-essential-training).
In this course the teacher teachs to create notes, but I changed to create motivacional phrases.


## Functionalities

* Home page with button that redirect to all phrases
* A page with all phrases.
* If you click at the title you can see the details about this phrase

## Comand lines

1. Create your virtual env
```
python3 -m venv .venv
```
2. Active the venv
```
source nameofyourvenv/bin/activate
```
3. Install the dependences
```
python3 -m pip install -r requirements.txt
```
4. Run the server
```
python3 manage.py runserver
```

## Routes

* notes - List all phrases
* notes/1 - see details about this phrase
* home - welcome page
* authorized - this area is just for superadmin


