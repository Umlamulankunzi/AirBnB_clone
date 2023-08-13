#!/usr/bin/python3
"""Module Defining User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
