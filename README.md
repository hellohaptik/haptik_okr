# haptik_okr
For OKR management tool


### Running OKR TOOL

`docker-compose up` will start the containers.

Update the [_.env_](haptik_okr/.sample_env) file with your settings.

Run `docker-compose build` whenever there are any changes in dependencies to update the containers.

#### Migrations:
`docker-compose run server python manage.py migrate` will run the migrations for django.