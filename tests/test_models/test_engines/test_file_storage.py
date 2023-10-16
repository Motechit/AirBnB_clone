#!/usr/bin/python3
"""This file is a module of the Unittests"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """This file is a module of the Unittests"""

    my_model = BaseModel()

    def testClassInstance(self):
        """It tests the class instance"""
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """It tests the save and reload fxn"""
        self.my_model.full_name = "BaseModel Instance"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(key in all_objs, True)

    def testStoreBaseModel2(self):
        """It tests the following functions; save, reload and update"""
        self.my_model.my_name = "First name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(bm_dict['my_name'], "First name")

        create1 = bm_dict['created_at']
        update1 = bm_dict['updated_at']

        self.my_model.my_name = "Second name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = bm_dict['created_at']
        update2 = bm_dict['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(bm_dict['my_name'], "Second name")

    def testHasAttributes(self):
        """It checks the existence of attributes"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testsave(self):
        """It checks if the JSON file exists"""
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testreload(self):
        """It handles reloads"""
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def testSaveSelf(self):
        """It checks save self """
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
