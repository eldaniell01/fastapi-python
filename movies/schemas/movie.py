from pydantic import BaseModel, Field
from typing import Optional, List

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=4, max_length=15)
    overview: str = Field(min_length=4, max_length=15)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=4, max_length=15)
    
    class Config:
        schema_extra ={
            "example": {
                'id': 1,
                'title': "mi pelicula",
                'overview': 'mi pelicula 2',
                'year': 2023,
                'rating': 9.9,
                'category': 'nueva'
            }
        }
