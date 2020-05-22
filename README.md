## Installation

Create virtual enviroment
```
python -m venv .env
```

Install requirements
```
pip install -r requirements.txt
```

Create tables in DB
```
python manage.py migrate
```

## Usage
Run server
```
python manage.py runserver
```


Create new course:
```
POST - http://127.0.0.1:8000/course/
```
Update course:
```
POST - http://127.0.0.1:8000/course/<id>/
```
### Add/remove students 
To add/remove students to a course, you need to add or remove a student’s ID in the variable "members" when updating the course data.

####For example:
We have Course:
```
{
    "members": [8,9],
    "title": "Course title",
    "description": "Course  description",
    "category": "Some category"
}
```

##### Add student to course:
```
PUT  -  http://127.0.0.1:8000/course/<course_id>/
```
With:
```
{
    "members": [8,9,10],
    "title": "Course title",
    "description": "Course  description",
    "category": "Some category"
}
```
, when 
"10" - id user

##### Remove student from course:
```
PUT  -  http://127.0.0.1:8000/course/<course_id>/
```
With:
```
{
    "members": [8],
    "title": "Course title",
    "description": "Course  description",
    "category": "Some category"
}
```

## Tests
Run tests
```
python manage.py test
```

## Change DB backend
To change the database backend, edit this section in the settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Example:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
