from fastapi import FastAPI, Body #Se importa el modulo fastapi con la clase FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Aprendiendo FastApi",
    description = "Una Api en los primeros pasos",
    version='0.0.1') #Se instancia la clase en la variable app

movies = [
    {
        'id': 1,
        'title': 'El Padrino',
        'overview': 'El Padrino es una película de 1972 dirigida por Francis Ford Coppola ...',
        'year': '1972',
        'rating':9.2,
        'category': 'Crimen'
    }
]
@app.get('/',tags=['Inicio']) #creamos el primer endpoint en el decorador
def read_root(): 
    return HTMLResponse('<h2>Hello world!</h2>') #retornamos un elemento HTML con HTMLResponse

@app.get('/movies',tags=['Movies'])
def get_movies():
    return movies

@app.get("/movies/{id}", tags=['Movies']) #Parametros de Ruta
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str):
    return category

@app.post("/movies", tags=['Movies'])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: str = Body(), rating: float = Body(), category: str = Body()):
    movies.append({"id": id, "title": title, "overview": overview, "year": year, "rating": rating, "category": category})
    return title

@app.put("/movies/{id}",tags=['Movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: str = Body(), rating: float = Body(), category: str = Body()):
    for item in movies:
        if item["id"] == id:
            item['title'] = title
            item['overview'] = overview
            item['year'] = year
            item['rating'] = rating
            item['category'] = category
            return movies

@app.delete("/movie/{id}", tags=['Movies'])
def delete_movie(id:int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return []
        