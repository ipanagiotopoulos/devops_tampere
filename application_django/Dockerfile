# Use an official Python runtime as a parent image
FROM python:3.9-alpine As dependecies
# Set environment variables
ENV PYTHONUNBUFFERED 1
# Set the working directory in the container
WORKDIR /application_django
# Copy the requirements file into the container
COPY /application_django/devops/requirements.txt .
#install python, gcc depencies
RUN apk update && apk add python3-dev \
    gcc \
    libc-dev
#essential pacakge for alpine containers in order to exec commands in a bash shell
RUN apk add --no-cache --upgrade bash
#upgrading pip
RUN pip install --upgrade pip
#install django app requirements
RUN pip install -r requirements.txt
# coping all the django web app file system to its respective container
COPY ./application_django/devops .
COPY ./logs/service1.log /application_django/logs/
#permissions for our script to run
RUN chmod +x init.sh
#entrypoint for our containarized web application run
CMD ["sh", "init.sh"]


