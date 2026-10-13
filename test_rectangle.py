
import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20)

    def test_area_zero(self):
        self.assertEqual(area(4, 0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(4, 5), 18)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(5, 5), 20)


if __name__ == '__main__':
    unittest.main()
