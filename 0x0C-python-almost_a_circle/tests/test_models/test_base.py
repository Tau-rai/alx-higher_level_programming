import unittest
import os
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):

    def setUp(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")

    def test_init(self):
        objct1 = Base()
        self.assertEqual(objct1.id, 1)

        objct2 = Base(3)
        self.assertEqual(objct2.id, 3)

        objct3 = Base(7)
        self.assertEqual(objct3.id, 7)

    def test_type(self):
        objct1 = Base()
        self.assertTrue(isinstance(objct1, Base))

if __name__ == "__main__":
    unittest.main()