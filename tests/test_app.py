import unittest
from app import greet
class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from Mohammad Jawad Al Masri!")

if __name__ == " main ":
    unittest.main()