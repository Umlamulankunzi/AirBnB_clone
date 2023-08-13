#!/usr/bin/python3


"""
Module defining class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import os
import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """FileStorage class that serializes instances to a JSON file and

    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialises new instance of FileStorge Class"""
        pass

    def all(self):
        """Returns the dictionary __objects

        Returns:
            dict: dict containing all created objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (any): any models package class
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        parsed_obj_dict = {}
        for key, obj in self.__objects.items():
            parsed_obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w+") as file:
            json.dump(parsed_obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file

        (__file_path) exists ; otherwise, do nothing. If the file doesn't
        exist, no exception should be raised)"""

        classes = {
            "Amenity": Amenity, "BaseModel": BaseModel, "City": City,
            "Place": Place, "Review": Review, "State": State,
            "User": User,
        }

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.load(file)

            for key, value in data.items():
                obj_class = classes[data[key]["__class__"]]
                self.__objects[key] = obj_class(**value)

    def delete_obj(self, obj_key):
        """deletes an instance

        Args:
            obj_key (str): key of instance
        """
        del self.__objects[obj_key]
