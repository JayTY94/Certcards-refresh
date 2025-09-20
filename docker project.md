Nice call — keep it small and focused. Below I’ll give you a complete minimal Dockerized Django “Hello World” app you can drop onto your Pi, build, and run. It uses Docker + docker compose, a tiny Django project (SQLite so no Postgres needed), and an nginx reverse proxy container so you can visit http://myapp.home from any device on your LAN (assuming you already added myapp.home -> 192.168.1.50 in Pi-hole).

Copy the files exactly as shown into a project directory on your Pi (I’ll use /home/pi/projects/docker-django-hello/ as an example).

What you’ll get

A web container that runs Django + Gunicorn

A proxy container running nginx that exposes port 80 on the Pi

A simple route / that returns “Hello from Dockerized Django!”

Project layout
docker-django-hello/
├─ app/
│  ├─ manage.py
│  ├─ requirements.txt
│  ├─ entrypoint.sh
│  ├─ myapp/
│  │  ├─ __init__.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  └─ wsgi.py
│  └─ core/
│     ├─ __init__.py
│     ├─ views.py
│     └─ urls.py
├─ deploy/
│  └─ nginx.conf
├─ Dockerfile
└─ docker-compose.yml

1) Dockerfile (put at repo root)
# Dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /usr/src/app/

# make entrypoint executable
RUN chmod +x /usr/src/app/entrypoint.sh

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]

2) docker-compose.yml (repo root)
version: "3.8"
services:
  web:
    build: .
    restart: unless-stopped
    volumes:
      - ./app:/usr/src/app
    environment:
      - ALLOWED_HOSTS=myapp.home,192.168.1.50,localhost
    expose:
      - "8000"

  proxy:
    image: nginx:stable
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - ./deploy/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - web

3) deploy/nginx.conf
server {
    listen 80;
    server_name myapp.home;

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://web:8000;
    }
}

4) app/requirements.txt
Django>=4.2,<5
gunicorn

5) app/entrypoint.sh (make executable)
#!/bin/bash
set -e

# apply migrations (sqlite will create db.sqlite3 automatically)
python manage.py migrate --noinput || true

# start the CMD (gunicorn)
exec "$@"


After creating it run:

chmod +x app/entrypoint.sh

6) Minimal Django app files

app/manage.py

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


app/myapp/__init__.py

# empty


app/myapp/settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "insecure-change-me")
DEBUG = os.environ.get("DEBUG", "1") == "1"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "core",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "myapp.urls"
WSGI_APPLICATION = "myapp.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]


app/myapp/urls.py

from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
]


app/myapp/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
application = get_wsgi_application()


app/core/__init__.py

# empty


app/core/views.py

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello from Dockerized Django on your Pi! 🎉")


app/core/urls.py

from django.urls import path
from .views import hello

urlpatterns = [
    path("", hello, name="hello"),
]

7) Build & run (commands you’ll run on the Pi)

From the repo root (/home/pi/projects/docker-django-hello/):

# build and start
docker compose up -d --build

# view logs if you want:
docker compose logs -f web
docker compose logs -f proxy


Then, from a client on your LAN that uses Pi-hole DNS, open:

http://myapp.home/


You should see: Hello from Dockerized Django on your Pi! 🎉

Notes & tips

This uses SQLite to keep things simple. When you later learn more, you can swap in Postgres (and add a db service to docker-compose.yml).

You mounted ./app into the container so you can edit code on your Pi and the container will pick up changes after restarting the container. For production-like behavior, remove the mount and COPY in the Dockerfile instead.

If the page doesn’t load:

confirm dig myapp.home returns your Pi’s LAN IP (Pi-hole).

docker compose ps to ensure containers are running.

docker compose logs web / docker compose logs proxy for errors.

On Raspberry Pi OS, the official python:3.11-slim image should work (multi-arch). If your Pi is older and you hit architecture issues, tell me the Pi model and I’ll adjust.

If you want, next steps I can provide (pick one):

Add a static assets route and have nginx serve /static/ (good next step).

Replace SQLite with a Postgres container and show environment variable handling.

Show how to run docker compose with an .env file and keep secrets out of the repo.

Convert this to a simple Dockerfile+compose that uses python manage.py runserver (dev mode) to make iterative editing even faster.