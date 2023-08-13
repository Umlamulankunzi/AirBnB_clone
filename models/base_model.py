#!/usr/bin/python3

"""
Module defining BaseModel class, which is a parent class to most of
models package classes.
"""

import datetime
import uuid
import models


class BaseModel:
    """Class that defines properties of BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialises new instance of BaseModel Class"""

        if kwargs:
            # print("initialising from dict")
            self.initialise_instance_from_kwargs(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def initialise_instance_from_kwargs(self, kwargs):
        """Initialises a new instance of BaseModel using dict argument

        Args:
            kwargs (dict): dict representation of BaseModel instance
        """
        for attribute, value in kwargs.items():
            if attribute == "__class__":
                continue
            elif attribute in ("created_at", "updated_at"):
                fmt = "%Y-%m-%dT%H:%M:%S.%f"
                str_to_datetime = datetime.datetime.strptime(
                    kwargs[attribute], fmt)
                setattr(self, attribute, str_to_datetime)

            else:
                setattr(self, attribute, value)

    def save(self):
        """Updates instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts a dictionary containing all keys/values of

        Returns:
            dict: attributes of instance object
        """
        instance_dict = {}
        datetime_keys_to_convert_to_isofmt = ("created_at", "updated_at")

        for key, value in self.__dict__.items():
            if key in datetime_keys_to_convert_to_isofmt:
                isofmt_datetime_obj = value.isoformat()
                instance_dict[key] = isofmt_datetime_obj
            else:
                instance_dict[key] = value
        instance_dict["__class__"] = self.__class__.__name__

        return instance_dict

    def __str__(self) -> str:
        """Returns string represantion of instance

        Returns:
            str: string represantation of instance
        """
        return f"[{self.__class__.__name__}] ({self.id }) {self.__dict__}"
