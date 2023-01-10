# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3
#makes sure that all output is in terminal 
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/

# Allows docker to cache installed dependencies between builds

RUN pip install  -r requirements.txt

# Mounts the application to the image
COPY . /code/


EXPOSE 8000
ENTRYPOINT [ "./entrypoint.sh" ]

# runs the production server
# ENTRYPOINT ["python", "manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]
# CMD echo python manage.py populate