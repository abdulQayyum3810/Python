# This file is for better understanding of setUp and tearDown methods

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    # This classmethod is run once before any test exectutes (ones before everything)
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass will run before everything\n")

    # This method is run once after all tests executes (once after everything)
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass will run after everything")
        
    # This method is run before every test case
    def setUp(self) -> None:
        print("setUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    # This method is run after every test case
    def tearDown(self) -> None:
        print("tearDown\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.fname = "Jhon"
        self.emp_2.fname = "Jane"

        self.assertEqual(self.emp_1.email, "Jhon.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.fname = "Jhon"
        self.emp_2.fname = "Jane"

        self.assertEqual(self.emp_1.fullname, "Jhon Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == "__main__":
    unittest.main()
