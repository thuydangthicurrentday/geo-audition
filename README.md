# Introduction

For the full project to work:

    git clone

# Run Backend

Then run your commands:

    pip install -r requirements.txt
    python manage.py migrate (migrate)
    python manage.py createsuperuser (user)
    python manage.py runserver

You can now visit the Swagger interface at:

    http://localhost:8000/webapi/swagger/

Note:

    Database used is sqlite

## Django Testing

To run django tests use the following command:

    python3 manage.py test

Tests are stored in each app.

## Running Tests

Tests could be run usings:

    python manage.py test apps.example.tests
    (python manage.py test apps.phonebook.tests)

## Class diagram

    docs\class-diagram.png
