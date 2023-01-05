# Scinet

## Crear entorno virtual e instalar dependencias
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
## Salir del entorno virtual
```
deactive
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
## Crear migraaciones y aplicarlas para docker-compose
```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```
## Correr docker server
```
docker-compose up
```