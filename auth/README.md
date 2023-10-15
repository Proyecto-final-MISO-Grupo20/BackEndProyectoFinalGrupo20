## Microservicio _Gestión de Usuarios_

Este microservicio se encarga de la autenticación de los usuarios. Sus funcionalidades son las siguientes:

- **Generación de tokens**: Proporcionando un nombre de usuario y una contraseña correcta, genera un token de autenticación al usuario 
- **Consulta la información de un usuario**: Retorna la información del usuario autenticado.
- **Consulta la salud del microservicio**: Permite verificar si el componente se está ejecutando.

Para mayor información consultar el siguiente enlace de la documentación.

[Documentación]()

## Estructura
````
├── auth # Archivos y directorios de la aplicación Usuarios
|   ├── config # Directorio con variables de entorno
|   ├── controllers # Directorio del controlador de la aplicación
|   ├── helpers # Directorio de inicialización de BD
|   ├── models # Directorio del modelo de la aplicación
|   ├── services # Directorio de los metodos de las funcionalidades de la app
|   ├── tests # Directorio de pruebas
|   ├── app.py # Archivo de inicialización de la aplicación
|   ├── database.py # Creación de la base de datos
|   ├── Dockerfile # Archivo de configuración de la imagen del componente
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

1) Ejecutar pruebas desde docker compose
```bash
docker-compose exec auth-microservice coverage run -m --omit="*/usr/lib/*" unittest discover -s tests
```

3) Obtener cobertura de pruebas desde docker compose
```bash
docker-compose exec auth-microservice coverage report -m --fail-under=80
```


