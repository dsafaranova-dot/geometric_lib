
import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3, 4, 5), 6)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_equilateral_area(self):
        self.assertAlmostEqual(area(2, 2, 2), 3**0.5)

    def test_equilateral_perimeter(self):
        self.assertEqual(perimeter(2, 2, 2), 6)


if __name__ == '__main__':
    unittest.main()
