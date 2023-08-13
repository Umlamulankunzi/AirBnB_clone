#!/usr/bin/python3
"""Module Defining Place class"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel class"""

    city_id = ""      # empty string: it will be the City.id
    user_id = ""      # empty string: it will be the User.id
    name = ""         # empty string
    description = ""  # empty string
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # will be list of Amenity.id later
