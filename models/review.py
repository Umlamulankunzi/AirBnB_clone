#!/usr/bin/python3


from models.base_model import BaseModel


class Review(BaseModel):
    
    place_id: str = ""  # empty string: it will be the Place.id
    user_id: str = ""   # empty string: it will be the User.id
    text: str = ""      # empty string