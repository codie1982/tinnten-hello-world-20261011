import unittest
from hello import greet


class GreetingTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, World!")
    
    def test_greet_none(self):
        self.assertEqual(greet(None), "Hello, World!")

    def test_named_greeting(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_unicode_name(self):
        self.assertEqual(greet("Çağrı"), "Hello, Çağrı!")


if __name__ == "__main__":
    unittest.main()
