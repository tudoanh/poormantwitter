ARG PYTHON_VERSION=3.9-slim-bullseye

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

# Install apt packages
RUN apt-get update && apt-get install sqlite3 -y

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip install -r requirements.txt

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ${APP_HOME}


COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# copy application code to WORKDIR
COPY . ${APP_HOME}
