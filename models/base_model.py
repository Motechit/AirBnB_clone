#!/usr/bin/python3
"""
Base_model.py defines all the attributes/methods
and serves as the base class for all other classes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """This is the base class"""
    def __init__(self, *args, **kwargs):
        """This is the initialization of the Base instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs:
            dtime_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], dtime_format)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], dtime_format)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """It returns a readable string rep.
        of BaseModel instances"""

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
        """It updates the public instance attribute updated at
        with the current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """It returns a dictionary that contains all
        keys/values of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
