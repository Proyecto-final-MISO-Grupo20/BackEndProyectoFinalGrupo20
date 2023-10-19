## Microservicio _Gestión de Ofertas_

Este microservicio se encarga de la gestión de las ofertas de la aplicación. Sus funcionalidades son las siguientes:

- **Creación de ofertas**: Permite la creación de ofertas a un usuario autenticado.
- **Listado de ofertas**: Permite realizar una búsqueda de ofertas realizadas a una publicación determinada.
- **Consulta de una oferta**: Permite a un usuario autenticado, obtener la información relacionada de una oferta.
- **Consulta la salud del microservicio**: Permite verificar si el componente se está ejecutando.

## Estructura
````
├── offers # Archivos y directorios de la aplicación Offers
|   ├── src # Directorio que contiene el código de la aplicación
|   ├── tests # Directorio de pruebas
|   ├── .coveragerc # Exclusión de archivos para las pruebas
|   ├── create_db_schema.py # Inicialización de la base de datos
|   ├── Dockerfile # Archivo de configuración de la imagen del componente
|   ├── main.py # Archivo de inicialización de la aplicación
|   ├── Pipfile # Dependencias de la aplicación
|   ├── Pipfile.lock # Archivo lock de dependencias
|   ├── README.md # Archivo con información útil de la aplicación
|   ├── requirements.txt # Archivo de dependencias de la aplicación
|   ├── run_service.sh # Archivo para la ejecución del servicio
````

**Pruebas Unitarias**
---
1) Ejecutar pruebas
```bash
coverage run -m pytest -s tests
```

2) Ejecutar pruebas desde docker compose
```bash
docker-compose exec offers-microservice coverage run -m pytest -s tests
```

3) Obtener cobertura de pruebas
```bash
coverage report -m
```

4) Obtener cobertura de pruebas desde docker compose
```bash
docker-compose exec offers-microservice coverage report -m
```