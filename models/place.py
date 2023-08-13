#!/usr/bin/python3
"""Module Defining Place class"""


from models.base_model import BaseModel


class Place(BaseModel):

    city_id: str = ""      # empty string: it will be the City.id
    user_id: str = ""      # empty string: it will be the User.id
    name: str = ""         # empty string
    description: str = ""  # empty string
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list[str] = []  # will be list of Amenity.id later
