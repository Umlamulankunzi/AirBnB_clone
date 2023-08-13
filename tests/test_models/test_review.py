#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_inheritance(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_attribute_types(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_attribute_defaults(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attribute_assignment(self):
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "This is a test review"
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "This is a test review")

    def test_str_representation(self):
        self.assertEqual(
            str(self.review),
            f"[Review] ({self.review.id}) {self.review.__dict__}"
        )


if __name__ == "__main__":
    unittest.main()
