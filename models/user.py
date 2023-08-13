#!/usr/bin/python3
"""Module Defining User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel class"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
