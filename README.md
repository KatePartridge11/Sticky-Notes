# Sticky Notes App

A simple web application built with Django that lets you create, view, edit, and delete sticky notes.

## Features
* Create new sticky notes.
* View a list of all your notes.
* Edit existing notes.
* Delete notes you no longer need.

## How to Run the App

1. **Set up and activate a virtual environment:**
   python -m venv venv
   .\venv\Scripts\Activate.ps1

2. **Install Django:**
   pip install django

3. **Set up Database:**
    python manage.py makemigrations
    python manage.py migrate

4. **Start the Sever:**
   python manage.py runserver

5. **Run Tests:**
   python manage.py test
