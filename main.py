from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List


# Estamos creando una instancia de FastApi
app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

# La clase Movie hereda de BaseModel
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating:float = Field(default=10, ge=1, le=10)
    category:str = Field(default='Categoría', min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category" : "Acción"
            }
        }

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


# Creamos el EndPoint
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


# Ruta de la lista completa de las peliculas
@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)




# Ruta que recibe un parametro (id) tambien realiza el filtrado en el estado de las peliculas por su id
@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
#Para poder acceder al parametro id que se esta recibiendo, se tiene que añadir a la función
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    #Filtrado de la pelicula mediante el id que se esta recibiendo
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])
    # return JSONResponse((next((item for item in movies if item["id"] == id),  {})))
    """
    Se retorna un dictionary comprehension La sintaxis completa 
    item for item in movies puede leerse como "para cada item en la 
    lista movies, incluir item en el nuevo diccionario". En otras 
    palabras, estamos creando un nuevo diccionario que contiene todos los 
    elementos de la lista movies, pero en un formato de diccionario.
    """


"""
Como el parametro no se especifico o definio en la url (en el 
parametro de ruta), automaticmente fastAPI va detectarlo como un 
parametro query (serie de clave valor).
"""
@app.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = [item for item in movies if item['category'] == category]    
    return JSONResponse(content=data)


@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})

@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return JSONResponse(status_code=200, content={"message": "Se ha actualizado la pelicula"})

@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(status_code=200, content={"message": "Se ha eliminado la pelicula"})

