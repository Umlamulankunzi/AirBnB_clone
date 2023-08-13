#!/usr/bin/python3

"""Module defining Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel class"""

    place_id: str = ""  # empty string: it will be the Place.id
    user_id: str = ""   # empty string: it will be the User.id
    text: str = ""      # empty string
