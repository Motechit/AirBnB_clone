#!/usr/bin/env python3
"""This is the Unittest module for the Amenity Class"""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import uuid
import datetime
import time
import re
import json
from models.engine.file_storage import FileStorage
from models import storage

class TestAmenity(unittest.TestCase):
    """This is the amenity model class test case"""

    @classmethod
    def setUpClass(cls):
        """It setups the unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        """It cleans up the dirt"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    a = Amenity()
    def test_has_attributes(self):
        """It checks the existence of the attributes"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_attributes_are_string(self):
        self.assertIs(type(self.amenity.name), str)

    def test_class_exists(self):
        """It checks the existence of the class"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_user_inheritance(self):
        """It checks if amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def test_types(self):
        """It checks if the attribute type is right"""
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.amenity))


if __name__ == "__main__":
    unittest.main()
