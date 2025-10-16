from fastapi import FastAPI, Body, Path #Se importa el modulo fastapi con la clase FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(
    title="Aprendiendo FastApi",
    description = "Una Api en los primeros pasos",
    version='0.0.1') #Se instancia la clase en la variable app

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Titulo de la pelicula",min_length=5, max_length=30) #validacion
    overview: str = Field(default="Descripción de la pelicula",min_length=15, max_length=80)
    year: int = Field(default=2023)
    rating: float = Field(ge = 1, le = 10) # ge significa mayor o igual, le significa menor o igual
    category: str = Field(default="Aquí va la categoría", min_length=3, max_length=60)
    
    
        
    
movies = [
    {
        'id': 1,
        'title': 'El Padrino',
        'overview': 'El Padrino es una película de 1972 dirigida por Francis Ford Coppola ...',
        'year': 1972,
        'rating':9.2,
        'category': 'Crimen'
    }
]
@app.get('/',tags=['Inicio']) #creamos el primer endpoint en el decorador
def read_root(): 
    return HTMLResponse('<h2>Hello world!</h2>') #retornamos un elemento HTML con HTMLResponse

@app.get('/movies',tags=['Movies'])
def get_movies():
    return JSONResponse(content= movies)

@app.get("/movies/{id}", tags=['Movies']) #Parametros de Ruta
def get_movie(id: int = Path(ge=1, le=100)):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['Movies'], status_code=200)
def get_movies_by_category(category: str):
    return category

@app.post("/movies", tags=['Movies'], status_code= 201)
def create_movie(movie: Movie):
    movies.append(movie.model_dump())
    return JSONResponse(content={'message': 'Se ha creado una nueva película','movies': [movie.dict() for m in movies]})

@app.put("/movies/{id}",tags=['Movies'], status_code=200)
def update_movie(id:int, movie:Movie):
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(content={'message':'Se ha modificado la pelicula'})
    return {"error": "Movie not found"}

@app.delete("/movies/{id}", tags=['Movies'], status_code=200)
def delete_movie(id:int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={'message':'Se ha eliminado una película'})
    