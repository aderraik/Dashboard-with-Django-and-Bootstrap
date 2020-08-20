FROM python:3.7.5-alpine

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./manage.py manage.py
COPY ./dashboard ./dashboard

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

LABEL maintainer="Andre Derraik <andre@albdconsult.com.br>"

CMD python manage.py runserver 0.0.0.0:8000
#CMD gunicorn -c gunicorn.py "app.wsgi:application"
