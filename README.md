# Scinet

## Crear entorno virtual e instalar dependencias
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
## Salir del entorno virtual
```
deactivate
```

## Ejecutar aplicación
```
python manage.py runserver
```

## Crear migraciones y aplicarlas
```
python manage.py makemigrations scinet_app
python manage.py migrate scinet_app
```
## Crear migraciones y aplicarlas para docker-compose
```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```
## Correr docker server
```
docker-compose up
```

## Llenar base de datos en docker
```
docker-compose run web python manage.py populate
```

## Running interactive shell in a docker container
```
docker exec -it <container-name> sh
```