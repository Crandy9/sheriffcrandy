# sheriffcrandy
Web app for independent music artist Sheriff Crandy. This is a full stack web app which uses Django, Django rest framework, token authentication, PostgreSQL and VUE.js for frontend.

(loosely followed this Django/Django Rest Framework/Vue.js tutorial as starting point: https://www.youtube.com/watch?v=Yg5zkd9nm6w)

The site's capabilities will include:
1.) music streaming, with the option of purchasing and downloading music files/fl studio .flp project files. 
2.) Payment processing handled by Stripe API payment gateway.
3.) user authentication/authorization handled by custom backend, custom user model, and Django rest framework via token authentication
4.) user cart implementaiton for purchasing multiple music files/.flp project files.
5.) i18n (internationalization) for Japan/United states locales
6.) Music Artist's portal to upload music and get paid

Future implementations can accomodate:
- mobile (android/iOS) development 
- Desktop app development
- additional region/locale support

Basic File Structure:
```
SHERIFFCRANDY-
            |
            repo (Django)-
                |
                main_project-
                            |
                            files....

                |
                flps -
                     |
                     files....
                |
                tracks -
                     |
                     files....
                |
                users -
                     |
                     files....
                |
                orders -
                       |
                       files...
                manage.py

            repo_vue (VueJS)-
                    |
                    basic VueJS directory

```


 Django setup:

- make dir on local machine where this project will be located

- clone this repo from github (ssh or https)

- Create python virtual environment on local machine: 

python3 -m venv env

- Activate python virtual environment on local machine: 

. env/bin/activate (you'll see '(env)' on the left-most side the terminal signature when activated)

- Once your env is activated, install Django and other dependencies:

- pip install django (the backend framework)
- pip install django-rest-framework (creating the backend API, creates djangorestframework dir as well)
- pip install djangorestframework-simplejwt (Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework. Updated framework from djangorestframework-jwt which is now deprecated)
- pip install pyjwt (Python library which allows you to encode and decode JSON Web Tokens JWT)
- pip install social-auth-app-django (for 3rd party auth Facebook, Google, LinkedIn, etc.)
- pip install django-cors-headers (provides security between backend and API)
- pip install pip install djoser (assists with user auth)
- pip install pillow (image processing)
- pip install pydub (audio file processing)
- pip install django-environ (for environment variables)
- pip install stripe (payment processor for handling secure payments)
- pip3 install --upgrade stripe (upgrade stripe)
- pip install psycopg2 (database adapter for PostgreSQL DB)
- install pgadmin4 desktop tool for DB management (https://www.pgadmin.org/download/)

*** Note: You need to create empty DB in either psql shell or pgadmin tool before running python manage.py makemigrations and python manage.py migrate (If you want to use custom user model, DO NOT RUN python manage.py makemigrations/migrate until you have created your custom user model, otherwise Django will revert to its default User Model. Changing from Django's default user model to a custom user model is possible, but unsupported and prone to many errors. Do this first before anything else if that's what you want for your app)
- activate env
(linux) . env/bin.activate
- create new Django project (make sure you are in dir you want project to be created):
django-admin startproject yourprojectname
- run python manage.py runserver to start django backend development server on localhost:8000
- create app (sub projects; make sure you are in project root directory)
python manage.py startapp my app name


 Vue.js setup:

- open a new terminal and cd to yourprojectname dir and install vue cli:
npm install -g @vue/cli (if you get a bunch of permission errors, run again with sudo)
- check installation:
vue --version

- in main dir (enter 'ls' and you should see LICENSE, README.md, repo) create vue project:
create vue_repo
- select manually select features:
Babel
Router
Vuex (for cart implementation)
CSS pre-processors
- unselect Linter/formatter (idk why, that's what they did in the tutorial lol)
- hit enter
- use 3.x version
- hit enter
- select 'Y' for router history mode and hit enter
- select Sass/SCSS (with dart-sass) and hit enter
- select 'place Babel, ESLint, etc. config files in dedicated config files'
- Select 'n' for saving this preset for future projects
- cd to repo_vue and install axios library used to access Django API data:
npm install axios
- install bulma (css framework)
npm install bulma
- install toast pop when adding items to cart
npm install bulma-toast
- install bulma modal-fx
npm i bulma-modal-fx
- install animate.css
npm install animate.css
- install i18n for internationalization (translating website)
npm install vue-i18n@next
- install vue-cli-plugin-i18n for internationalization (if you have Vue Cli 3.x) https://kazupon.github.io/vue-i18n
vue add i18n
- will install the following:
- .env vars: 
VUE_APP_I18N_LOCALE=en
VUE_APP_I18N_FALLBACK_LOCALE=en
- update dependcies in:
repo_vue/package-lock.json
repo_vue/package.json
- create new files:
repo_vue/vue.config.js
repo_vue/src/i18n.js
- import i18n in main.js
- create repo_vue/src/components/HelloI18n.vue (may not need it)
- create json files to hold translations repo_vue/src/locales/en.json

- to run vue app on localhost:8080 
npm run serve
