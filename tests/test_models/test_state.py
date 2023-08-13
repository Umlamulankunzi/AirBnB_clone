#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_inheritance(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        self.assertEqual(self.state.name, "")

    def test_attribute_types(self):
        self.assertIsInstance(self.state.name, str)

    def test_attribute_defaults(self):
        self.assertEqual(self.state.name, "")

    def test_attribute_assignment(self):
        self.state.name = "Alx_State"
        self.assertEqual(self.state.name, "Alx_State")

    def test_str_representation(self):
        self.assertEqual(
            str(self.state),
            f"[State] ({self.state.id}) {self.state.__dict__}"
        )


if __name__ == "__main__":
    unittest.main()
