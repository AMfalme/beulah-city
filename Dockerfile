# Use an official Python runtime as a parent image
FROM python:3.7

#Set build variables, needed for running migrations
#SECURITY_TODO: Secrets should not be exposed
ARG WAGTAIL_DB_USER=mizizi
ARG WAGTAIL_DB_PASS=gzlGFzYN%6a4!u7
ARG WAGTAIL_DB_HOST=mizizi-postgres.do.mizizi.io
ARG WAGTAIL_DB_PORT=5432

ARG BEULAH_WAGTAIL_DB=beulahcity_com
ARG BEULAH_SECRET_KEY=aJ41Zrj&oFkv*R5$8IkGlG0Ct*1LiyAo
ARG DJANGO_SETTINGS_MODULE=beulahcity.settings.production

ARG BEULAH_AWS_STORAGE_BUCKET_NAME=wagtail-beulahcity-com
ARG AWS_ACCESS_KEY_ID=AKIAQM76M46W6BNFMP6A
ARG AWS_SECRET_ACCESS_KEY=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

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production 

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install uwsgi

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

RUN python manage.py migrate
RUN python manage.py collectstatic

RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000
CMD exec uwsgi --ini uwsgi.ini
