import unittest
import os
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_inheritance(self):
        Rect = Rectangle(7, 4)
        self.assertIsInstance(Rect, Rectangle)

    def test_Rectangle_init(self):
        rect1 = Rectangle(7, 3)
        self.assertEqual(rect1.id, 3)

        rect2 = Rectangle(2, 9)
        self.assertEqual(rect2.id, 4)

        rect3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect3.id, 12)

    def test_area(self):
        rect1 = Rectangle(7, 3)
        self.assertEqual(rect1.area(), 21)

    def test_Rectangle_typeError(self):
        Rect = Rectangle(7, 5)
        with self.assertRaises(TypeError):
            Rect.width = "unknown"

    def test_Rectangle_valueError(self):
        Rect = Rectangle(9, 3)
        with self.assertRaises(ValueError):
            Rect.width = 0
    
    def test_zero_values(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_Rectangle_str_rep(self):
        Rect = Rectangle(5, 9, 2, 3, 1)
        self.assertEqual(str(Rect), "[Rectangle] (1) 2/3 - 5/9")

    def test_Rectangle_update_args(self):
        Rect = Rectangle(5, 9, 2, 3, 1)
        Rect.update(7, 27, 37, 17, 57)
        self.assertEqual(Rect.id, 7)
        self.assertEqual(Rect.width, 27)
        self.assertEqual(Rect.height, 37)
        self.assertEqual(Rect.x, 17)
        self.assertEqual(Rect.y, 57)

    def test_Rectangle_to_dictionary(self):
        Rect = Rectangle(5, 9, 2, 3, 1)
        exp_dict = {'id': 1, 'width': 5, 'height': 9, 'x': 2, 'y': 3}
        self.assertEqual(Rect.to_dictionary(), exp_dict)

    def test_to_json_string(self):
        obj = Rectangle(1, 2)
        res = Base.to_json_string([obj.to_dictionary()])
        self.assertEqual(res, '[{"id": 18, "width": 1, "height": 2, "x": 0, "y": 0}]')

        res = Base.to_json_string(None)
        self.assertEqual(res, '[]')

    def test_save_to_file(self):
        obj1 = Rectangle(1, 7)
        Base.save_to_file([obj1])

        self.assertTrue(os.path.exists("Base.json"))

        with open("Base.json", "r") as f:
            cont = f.read()
            self.assertEqual(cont, '[{"id": 17, "width": 1, "height": 7, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        res = Base.from_json_string(json_string)
        self.assertEqual(res, [{'id': 1}, {'id': 2}])

        res = Base.from_json_string(None)
        self.assertEqual(res, [])

    def test_update_with_incorrect_arguments(self):
        Rect = Rectangle(5, 9, 2, 3, 1)
        with self.assertRaises(TypeError):
            Rect.update(width="unknown")

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)
        with self.assertRaises(TypeError):
            Rectangle(2, 1.5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1.5, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1, 2.5)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 1, -2)

    # def test_create(self):
    #     obj = Base.create(id=5)
    #     self.assertEqual(obj.id, 5)

    #     obj = Rectangle.create(id=1, width=2, height=3, x=4, y=5)
    #     self.assertEqual(obj.id, 1)
    #     self.assertEqual(obj.width, 2)
    #     self.assertEqual(obj.height, 3)
    #     self.assertEqual(obj.x, 4)
    #     self.assertEqual(obj.y, 5)

    # def test_load_from_file(self):
    #     obj1 = Rectangle(7, 3)
    #     obj2 = Rectangle(5, 3)
    #     Base.save_to_file([obj1, obj2])

    #     res = Base.load_from_file()
    #     self.assertEqual(res, [obj1, obj2])

if __name__ == "__main__":
    unittest.main()