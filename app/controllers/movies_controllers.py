from fastapi import APIRouter
from app.services import MoviesService
from app.schemas import Movie


router = APIRouter(prefix="/movies", tags=["Movies"])

service = MoviesService()

# @router.get('/')
# def get_prueba():
#   return "Hola Mundo"

#http://127.0.0.1:8000/api/v1/movies/films
@router.get('/films')
def get_movies():
  return service.get_movies()	


@router.get('/films/{movie_id}')
def get_movie(movie_id:int):
  return service.get_movie(movie_id)  

@router.post('/films')
def create_movie(movie:Movie):
  return service.create_movie(movie)


@router.put('/films/{movie_id}')
def update_movie(movie_id:int, movie:Movie):
  return service.update_movie(movie_id, movie)


@router.delete('/films/{movie_id}')
def delete_movie(movie_id:int):
  return service.delete_movie(movie_id)


