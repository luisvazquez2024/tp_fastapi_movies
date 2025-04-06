from fastapi import HTTPException
from app.repositories.database import movies
from app.schemas import Movie

class MoviesRepository:
		def __init__(self):
				self.movies = movies
		
		
		def get_movies(self):
				return self.movies
  
		def get_movie(self, movie_id:int):
				if not movie_id in range(len(self.movies)):
						raise HTTPException(status_code=404, detail="Movie not found")
				return self.movies[movie_id]	
  
  
		def create_movie(self, movie:Movie):
				self.movies.append(movie.model_dump())
				return self.movies[-1]
  
  
		def update_movie(self, movie_id:int,movie:Movie):
			if not movie_id in range(len(self.movies)):
					raise HTTPException(status_code=404, detail="Movie not found")
			self.movies[movie_id] = movie.model_dump()
			return self.movies[movie_id]
 
 
		def delete_movie(self, movie_id:int):
			if not movie_id in range(len(self.movies)):
					raise HTTPException(status_code=404, detail="Movie not found")
			self.movies.pop(movie_id)
			return self.movies
    