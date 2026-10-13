import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(1), 3.141592653589793)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * 3.141592653589793)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()
