#!/usr/bin/python3


import unittest
import time
from datetime import datetime
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        # initially it executed this test so fast that even after
        # calling save() method on instance the datetimes were equal
        time.sleep(0.000001)
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)

    def test_to_dict_contains_all_attributes(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    def test_to_dict_datetime_format(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

    def test_str_representation(self):
        self.assertEqual(
            str(self.base_model),
            f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        )


if __name__ == '__main__':
    unittest.main()