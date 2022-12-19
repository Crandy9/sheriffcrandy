# sheriffcrandy
Web app for independent music artist Sheriff Crandy. This will be a full stack web app using Django web framework, Django REST API, and VUE.js for the frontend.

(follwed this Django/Django Rest Framework/Vue.js tutorial as starting point here: https://www.youtube.com/watch?v=Yg5zkd9nm6w)

The site's capabilities will include music streaming, with the option of purchasing and downloading song files. Payment processing will be handled by Stripe.

Basic File Structure:

SHERIFFCRANDY-
            |
            repo-
                |
                main_project-
                            |
                            __init__.py
                            .env
                            asgi.py
                            settings.py
                            urls.py
                            wsqi.py
                manage.py
            repo_vue-
                    |
            .gitignore
            LICENSE
            README.md


Django backend setup:
- make dir on local machine where this project will be stored

- clone this repo from github

- Create and activate python virtual environment on local machine: 

python3 -m venv env

- Once your venv is activated, install Django and other dependencies:

pip install django (the backend framework)
pip install django-rest-framework (creating the backend API)
pip install django-cors-headers (provides security between backend and API)
pip install pip install djoser (assists with user auth)
pip install pillow (image processing)
pip install django-environ (for environment variables)
pip install stripe (payment processor for handling secure payments)
pip install psycopg2 (database adapter for PostgreSQL DB)
install pgadmin4 desktop tool for DB management (https://www.pgadmin.org/download/)
Note: need to create empty DB in either psql shell or pgadmin tool before running python manage.py makemigrations and python manage.py migrate
- create new Django project:
django-admin startproject yourprojectname


Vue.js setup:

- open a new terminal and cd to yourprojectname dir and install vue cli:
npm install -g @vue/cli (if you get a bunch of permission errors, run again with sudo)
- check installation:
vue --version

- in main dir (enter 'ls' and you should see LICENSE  README.md  repo) create vue project:
create vue_repo
- select manually select features:
Babel
Router
Vuex
CSS pre-processors
- unselect Linter/formatter (idk why, that's what they did in the tutorial lol)
- hit enter
- use 3.x version
- hit enter
- select 'Y' for router history mode and hit enter
- select Sass/SCSS (with dart-sass) and hit enter
- place Babel, ESLint, etc. config files in dedicated config files
- Select 'n' for saving this preset for future projects
- cd to repo_vue and install axios library used to talk to backend:
npm install axios
- install bulma (css framework)
npm install bulma