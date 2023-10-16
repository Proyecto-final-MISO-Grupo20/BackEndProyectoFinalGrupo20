# Proyecto Final Grupo20

Repositorio para el Backend del proyecto final de la Maestría en Ing. de software de la Universidad de los Andes.

# Integrantes

- Estefania Fajardo: a.fajardor@uniandes.edu.co
- Juan Jose Ochoa Ortiz: j.ochoao@uniandes.edu.co
- Rafael Ortiz: rd.ortizr1@uniandes.edu.co
- Cesar Rivera: c.riverao@uniandes.edu.co

# Estructura
````

|── .github/workflows
|   └── ci_pipeline.yml # Configuración del pipeline
├── auth # Archivos del microservicio de usuarios
├── .gitignore # Exclusión de archivos del repositorio
├── docker-compose.yml # Archivo de definición de servicios, redes y volúmenes de la aplicación
├── Pipfile # Dependencias de la aplicación
├── Pipfile.lock # Archivo lock de dependencias
└── README.md # Estás aquí
````

## Cómo ejecutar la aplicación

Para ejecutar localmente se debe correr el siguiente comando, habiendo previamente instalado Docker.

```
docker compose up --build

```
