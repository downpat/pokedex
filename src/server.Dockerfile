FROM python:3.14-slim-trixie

WORKDIR /pokedex/src

RUN apt-get update
RUN apt-get install -y libpq-dev

RUN pip install psycopg2-binary==2.9.11
RUN pip install Django==4.2.24 #Pin Django to latest LTS
RUN pip install ipython
RUN pip install requests
RUN pip install celery[redis]

COPY ./ /pokedex/src

WORKDIR /pokedex/src/code/pokedex

CMD ["python", "run.py"] 
