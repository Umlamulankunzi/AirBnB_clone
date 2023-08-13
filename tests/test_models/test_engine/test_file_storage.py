#!/usr/bin/python3

import json
import os

import unittest
from models.base_model import BaseModel
from models.city import City

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"  # Use a different file for testing
        self.storage = FileStorage()
        # Override file path for testing
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        # Test if all() returns an empty dictionary initially
        self.assertEqual(self.storage.all(), {})

        # Create some test objects
        obj1 = BaseModel()
        obj2 = City()

        # Add objects to storage
        self.storage.new(obj1)
        self.storage.new(obj2)

        # Test if all() returns the correct dictionary
        expected_dict = {
            f"{obj1.__class__.__name__}.{obj1.id}": obj1,
            f"{obj2.__class__.__name__}.{obj2.id}": obj2,
        }
        self.assertEqual(len(self.storage.all()), len(expected_dict))

    def test_new(self):
        # Create a test object
        obj = BaseModel()

        # Add object to storage
        self.storage.new(obj)

        # Test if the object is added correctly
        expected_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(expected_key, self.storage.all())

    def test_delete_obj(self):
        # Create a test object
        obj = BaseModel()

        # Add object to storage
        self.storage.new(obj)

        # Test if the object exists in storage
        expected_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(expected_key, self.storage.all())

        # Delete the object
        self.storage.delete_obj(expected_key)

        # Test if the object is removed from storage
        self.assertNotIn(expected_key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
