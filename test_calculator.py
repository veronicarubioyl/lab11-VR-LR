# https://github.com/veronicarubioyl/lab11-VR-LR.git
# Partner 1: Veronica Rubio
# Partner 2: Lucas Rosen

import math
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-1,-1),-2)
        self.assertAlmostEqual(add(0.1,0.2),0.3)

    def test_subtract(self):
        self.assertEqual(subtract(5,3),2)
        self.assertEqual(subtract(3,5),-2)
        self.assertEqual(subtract(0,0),0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(-2,4), -8)
        self.assertEqual(multiply(0,5), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2,10),5.0)
        self.assertAlmostEqual(div(4,-8), -2.0)
        self.assertAlmostEqual(div(2,5), 2.5)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2,8),3.0)
        self.assertAlmostEqual(logarithm(10,100),2.0)
        self.assertAlmostEqual(logarithm(2,1),0.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1,8)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2,0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 7), 7.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(9),3.0)
        self.assertAlmostEqual(square_root(0), 0.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()