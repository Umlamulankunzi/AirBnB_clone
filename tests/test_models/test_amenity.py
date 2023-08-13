#!/usr/bin/python3


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_name_default_value(self):
        self.assertEqual(self.amenity.name, "")

    def test_name_type(self):
        self.assertIsInstance(self.amenity.name, str)

    def test_name_assignment(self):
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_inherited_attributes(self):
        self.assertIn('id', self.amenity.__dict__)
        self.assertIn('created_at', self.amenity.__dict__)
        self.assertIn('updated_at', self.amenity.__dict__)

    def test_str_representation(self):
        self.assertEqual(
            str(self.amenity),
            f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        )


if __name__ == '__main__':
    unittest.main()
