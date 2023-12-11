import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_inheritance(self):
        sqr = Square(7)
        self.assertIsInstance(sqr, Square)
        
    def test_square_init(self):
        sqr1 = Square(7, 5, 3, 1)
        self.assertEqual(sqr1.size, 7)
        self.assertEqual(sqr1.width, 7)
        self.assertEqual(sqr1.height, 7)
        self.assertEqual(sqr1.x, 5)
        self.assertEqual(sqr1.y, 3)
        self.assertEqual(sqr1.id, 1)

    def test_area(self):
        sqr1 = Square(3, 3)
        self.assertEqual(sqr1.area(), 9)

    def test_square_typeError(self):
        sqr = Square(7)
        with self.assertRaises(TypeError):
            sqr.size = "unknown"

    def test_square_valueError(self):
        sqr = Square(9)
        with self.assertRaises(ValueError):
            sqr.size = 0

    def test_square_str_rep(self):
        sqr = Square(5, 2, 3, 1)
        self.assertEqual(str(sqr), "[Square] (1) 2/3 - 5")

    def test_square_update_args(self):
        sqr = Square(5, 2, 3, 1)
        sqr.update(7, 27, 17, 57)
        self.assertEqual(sqr.id, 7)
        self.assertEqual(sqr.size, 27)
        self.assertEqual(sqr.x, 17)
        self.assertEqual(sqr.y, 57)

    def test_square_to_dictionary(self):
        sqr = Square(5, 2, 3, 1)
        exp_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(sqr.to_dictionary(), exp_dict)


if __name__ == "__main__":
    unittest.main()