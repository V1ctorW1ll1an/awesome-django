# Awesome project - django CMS

This version uses Python running and the most up-to-date versions of Django 3.1 and django CMS 3.8.

This project is 3.9.5

## Installation

You need to have docker installed on your system to run this project.

-   [Install Docker](https://docs.docker.com/engine/install/) here.
-   If you have not used docker in the past, please read this [introduction on docker](https://docs.docker.com/get-started/) here.

## Try it

```bash
git clone git@github.com:V1ctorW1ll1an/awesome-django.git
cd awesome-django
docker-compose build web
docker-compose up -d database_default
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up -d
```

Note: Since Compose V2, `docker-compose` is now included inside docker. For more information, checkout the [Compose V2](https://docs.docker.com/compose/cli-command/) Documentation.

#### Updating requirements

The project uses a 2 step approach, freezing all dependencies with pip-tools. Read more about how to handle it here: https://blog.typodrive.com/2020/02/04/always-freeze-requirements-with-pip-compile-to-avoid-unpleasant-surprises/
