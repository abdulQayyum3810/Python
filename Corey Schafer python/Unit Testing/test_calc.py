import unittest
import calc

# Best practices:  All test should be isolated (indpendent of each other)
class TestCacl(unittest.TestCase):

    # test methods should have prefix "test_" otherwise they will be skipped
    # https://docs.python.org/3/library/unittest.html#test-cases
    # python3 -m unittest test_calc.py  >> we run unittest module and pass it test file

    # Write good tests instead of a lot of tests
    # whenever caught an error during debug add it to test_cases
    def test_add(self):
        # Try to cover all edge casses if any of edge case fails test status will be failed
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        # Try to cover all edge casses if any of edge case fails test status will be failed
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        # Try to cover all edge casses if any of edge case fails test status will be failed
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        # Try to cover all edge casses if any of edge case fails test status will be failed
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 10), .5)
       
        # Checking raises 
        self.assertRaises(ValueError, calc.divide, 10, 0)
        # Better way to check raises
        with self.assertRaises(ValueError):
            calc.divide(10,0)


if __name__ == "__main__":
    # To get rid of running module now we can run our file directly
    unittest.main()
