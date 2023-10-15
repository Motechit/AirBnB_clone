#!/usr/bin/python3
"""File_storage.py utilizes JSON to serialize
and deserialize instances of an obj"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class FileStorage:
    """This class serializes and deserializes instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """It returns the dictionary of objs"""
        return type(self).__objects

    def new(self, obj):
        """It sets new obj in __objects dict."""
        if obj.id in type(self).__objects:
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """It serializes __objects to the JSON file (path: __file_path)"""
        new_dict = []
        for obj in type(self).__objects.values():
            new_dict.append(obj.to_dict())
        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """It deserializes the JSON file to __objects if it exists"""
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as file:
                    new_obj = json.load(file)
                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        type(self).__objects[key] = obj
            except Exception:
                pass
