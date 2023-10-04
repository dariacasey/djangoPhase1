Pre-requisites: \
    - Python (3.11.4)\
    - Pip (Package manager)

Steps: \
    1. Extract content of zip file \
    2. Navigate to project directory 

     cd directory-where-extracted-project/djangoProject/website
\
    3. Create virtual environment 

        python -m venv env 
\
    4. Activate the environment \
        - Mac/Linux 

        source env/bin/activate 
\
        - Windows 

        source env/Scripts/activate 
\
    5. Install Django 

        - pip install Django 
\
    6. Install dependencies 

        pip install Pillow 
        pip install django-ckeditor 
        pip install python-decouple 
\
    7. Run the server and view the site on your local host 

        python manage.py runserver
