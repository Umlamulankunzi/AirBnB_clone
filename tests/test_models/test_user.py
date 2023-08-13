#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attribute_types(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_attribute_defaults(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attribute_assignment(self):
        self.user.email = "test@alx.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Of_Alx"
        self.assertEqual(self.user.email, "test@alx.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Of_Alx")

    def test_str_representation(self):
        self.assertEqual(
            str(self.user),
            f"[User] ({self.user.id}) {self.user.__dict__}"
        )


if __name__ == "__main__":
    unittest.main()