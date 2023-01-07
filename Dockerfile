# Dockerfile

# We Use an official Python runtime as a parent image
FROM python:3

# Makes sure that all output is in terminal 
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
COPY base.py /code/

# Allows docker to cache installed dependencies between builds
RUN pip install  -r requirements.txt

# Mounts the application to the image
COPY . /code/


EXPOSE 8000
# ENTRYPOINT [ "./entrypoint.sh" ]

