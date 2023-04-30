from models.movie import Movie as mov
from schemas.movie import Movie

class MovieService():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_movie(self):
        result = self.db.query(mov).all()
        return result
    
    def get_movie1(self, id):
        result = self.db.query(mov).filter(mov.id ==id).first()
        return result
    
    def get_category(self, category):
        result = self.db.query(mov).filter(mov.category == category).all()
        return result
    
    def create_movie(self, movie: Movie):
        new = mov(**movie.dict())
        self.db.add(new)
        self.db.commit()
        return
    
    def update_movie(self, id: int, movie:Movie):
        result = self.get_movie1(id)
        result.title = movie.title
        result.overview = movie.overview
        result.year = movie.year
        result.rating = movie.rating
        result.category = movie.category
        self.db.commit()
        return

    def delete_movie(self, id: int):
        result = self.get_movie1(id)
        self.db.delete(result)
        self.db.commit()
        return