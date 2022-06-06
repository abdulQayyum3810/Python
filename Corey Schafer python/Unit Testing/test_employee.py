import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    
    # This classmethod is run once before any test exectutes (ones before everything)
    @classmethod
    def setUpClass(cls) -> None:
        pass

    # This method is run once after all tests executes (once after everything)
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    
    # This method is run before every test case
    def setUp(self) -> None:
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    # This method is run after every test case
    def tearDown(self) -> None:
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.fname = "Jhon"
        self.emp_2.fname = "Jane"

        self.assertEqual(self.emp_1.email, "Jhon.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.fname = "Jhon"
        self.emp_2.fname = "Jane"

        self.assertEqual(self.emp_1.fullname, "Jhon Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    # MOCKING
    # Sometimes certain things are not in our control (request form a website will not responsed if website is down 
    # but website is not in our control, only want that our code behaves correctly). But we still want to test our 
    # code, to fullfill this requirement mocking is used
    
    # patch mocks the object during test and restore the object after test is run it can be used as decorator or
    # context manager
    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok=True
            mocked_get.return_value.text="Success"
            
            # For successful request
            schedule=self.emp_1.monthly_schedule("May")
            # Mock objects records when and with what values they were called
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")
            
            #for failed request
            mocked_get.return_value.ok=False
            schedule=self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")
            
if __name__ == "__main__":
    unittest.main()
