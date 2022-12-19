# sheriffcrandy
Web app for independent music artist Sheriff Crandy. This will be a full stack web app using Django web framework, Django REST API, and VUE.js for the frontend.

(follwed this Django/Django Rest Framework/Vue.js tutorial as starting point here: https://www.youtube.com/watch?v=Yg5zkd9nm6w)

The site's capabilities will include music streaming, with the option of purchasing and downloading song files. Payment processing will be handled by Stripe.

To get started:

- make dir on local machine where this project will be stored

- clone from github

- Create and activate virtual environment on local machine: 

python3 -m venv env

- Once your venv is activated, install Django and dependencies:

pip install django (the backend framework)
pip install django-rest-framework (creating the backend API)
pip install django-cors-headers (provides security between backend and API)
pip install pip install djoser (assists with user auth)
pip install pillow (image processing)
pip install django-environ (for environment variables)
pip install stripe (payment processor for handling secure payments)

- create new Django project:
django-admin startproject yourprojectname