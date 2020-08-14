FROM python:3.6-alpine

# Variable de entorno

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev
# RUN apk add py-mysqldb
COPY . ./django
WORKDIR ./
RUN pip install django-bootstrap4
RUN pip install requests
RUN pip install django-crispy-forms
CMD python django/manage.py runserver 0.0.0.0:80

EXPOSE 80