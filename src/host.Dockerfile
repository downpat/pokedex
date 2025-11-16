FROM python:3.14-slim-trixie

WORKDIR /pokedex/src

RUN pip install celery[redis]


