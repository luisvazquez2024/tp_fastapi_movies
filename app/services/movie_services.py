from app.repositories import MoviesRepository
from app.schemas import Movie


class MoviesService:
	def __init__(self):
			self.repository:MoviesRepository = MoviesRepository();
	
   
	def get_movies(self):
			return self.repository.get_movies()
   
   
	def get_movie(self,movie_id):
			return self.repository.get_movie(movie_id)

	
	def create_movie(self, movie:Movie):
			return self.repository.create_movie(movie)
	
 
	def update_movie(self,movie_id:int, movie:Movie):
			return self.repository.update_movie(movie_id,movie) 
 
 
	def delete_movie(self,movie_id:int):
				return self.repository.delete_movie(movie_id)