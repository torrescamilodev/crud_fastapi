from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI() # Estamos creando una instancia de FastApi
app.title = "Mi aplicaión con FastAPI"
app.version = "0.0.1"

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]


@app.get('/', tags=['home']) # Creamos el EndPoint
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    #Este es un parametro de ruta donde se pide un valor
    
    # for item in movies:
    #     if item["id"] == id:
    #         return item
    # return []
    return next((item for item in movies if item["id"] == id), {})
#Se retona un dictionary comprehension La sintaxis completa item for item in movies puede leerse como "para cada item en la lista movies, incluir item en el nuevo diccionario". En otras palabras, estamos creando un nuevo diccionario que contiene todos los elementos de la lista movies, pero en un formato de diccionario.

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category:str, year:int):
    #Como el parametro no se especifico o definio en la url, en el parametro de ruta  automaticmente fastAPI va  detectarlo como un parametro query
    return category

# Para correr la aplicacion usamos el comando 'uvicorn main:app' y si queremos que se recargue automaticamente agregamos depues de app '--reload' y para asignarle un puerto '--port numero_del_puerto' y para que se pueda ver en toda la red '--host 0.0.0.0