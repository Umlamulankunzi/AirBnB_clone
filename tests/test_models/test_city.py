#!/usr/bin/python3


import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_state_id_default_value(self):
        self.assertEqual(self.city.state_id, "")

    def test_name_default_value(self):
        self.assertEqual(self.city.name, "")

    def test_state_id_type(self):
        self.assertIsInstance(self.city.state_id, str)

    def test_name_type(self):
        self.assertIsInstance(self.city.name, str)

    def test_state_id_assignment(self):
        self.city.state_id = "CA"
        self.assertEqual(self.city.state_id, "CA")

    def test_name_assignment(self):
        self.city.name = "City of Alx"
        self.assertEqual(self.city.name, "City of Alx")

    def test_inherited_attributes(self):
        self.assertIn('id', self.city.__dict__)
        self.assertIn('created_at', self.city.__dict__)
        self.assertIn('updated_at', self.city.__dict__)

    def test_str_representation(self):
        self.assertEqual(
            str(self.city),
            f"[City] ({self.city.id}) {self.city.__dict__}"
        )


if __name__ == '__main__':
    unittest.main()
