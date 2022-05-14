# Awesome project - django CMS

This version uses Python running and the most up-to-date versions of Django 3.1 and django CMS 3.8.

This project use python 3.9

## Installation

You need to have docker installed on your system to run this project.

-   [Install Docker](https://docs.docker.com/engine/install/) here.
-   If you have not used docker in the past, please read this [introduction on docker](https://docs.docker.com/get-started/) here.

## Try it

```bash
git clone git@github.com:V1ctorW1ll1an/awesome-django.git
cd awesome-django
docker-compose up -d database_default
docker-compose up -d
docker-compose exec -it /bin/sh
inside sh run:
  python manage.py createsuperuser
```

Note: [docker-compose](https://docs.docker.com/compose/cli-command/) 

#### Updating requirements

The project uses a 2 step approach, freezing all dependencies with pip-tools. Read more about how to handle it here: https://blog.typodrive.com/2020/02/04/always-freeze-requirements-with-pip-compile-to-avoid-unpleasant-surprises/
