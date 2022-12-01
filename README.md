# Scinet

## Crear entorno virtual e instalar dependencias
```
python -m venv env
source env/bin/activate
pip install django-environ
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
