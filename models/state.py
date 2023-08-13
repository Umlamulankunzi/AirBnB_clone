#!/usr/bin/python3
"""Module Defining State class"""


from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel class"""
    name: str = ""
