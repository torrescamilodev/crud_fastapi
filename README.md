# CRUD FastAPI
CRUD con Python y FasAPI

***Path Operation:*** Metodos HTTP
- Get
- Post
- Put
- Delete

Python siempre fue conocido por ser un lenguaje de programacion un poco lento al momento de crear API's, en comparacion con otros frameworks de otros lenguajes de programacion, es ahi donde nace la idea de crear FastApi el cual es un framework moderno y de alto rendimiento para creacion de API con python (toma lo mejor del ecosistema de python, frameworks y librerias ya existentes)

**Caracteristicas:**
-Rápido: a nivel de aprendizaje y rendimiento
-Robusto: Permite tener un codigo listo para producción, incluyendo la documentacion autogenerada con Swagger
-Basado en estándares: OpenAPI

**Marco utilizado por FastAPI:**
-Starlette: Framework Asincrono para construccion de servicios (Es uno de los mas rapidos de python)
-Pydantic: Validaciones de datos
-Uvicorn: Ejecutar las aplicaciones con FastApi


pydantic nos permite crear un esquema de datos que contenga toda la informacion relacionada a una pelicula.

Errores que muestras fasAPI: value error
validaciones con pydantic Field
parametros de ruta y de query con Path, Query de FastAPI