import logging

# Getting new logger __name__ (can be other name) and logger variable will be used to apply logging methods
logger = logging.getLogger(__name__)
# if some configuration is not set for our new logger it will fall back to root logger for that configuration


logger.setLevel(logging.INFO)  # Setting level for our new logger
file_handler = logging.FileHandler("Employee.log")  # Create file handler
# Getting a formator object for our handler (file or stream or any other handler)
formatter = logging.Formatter("%(levelname)s: %(name)s: %(message)s")
file_handler.setFormatter(formatter)  # Setting format for our file handler
logger.addHandler(file_handler)  # Add file handler to our logger

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # using logger instead of logging
        logger.info(f"Created Employee: {self.fullname} - {self.email}")

    @property  # getter
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    @property  # getter
    def email(self):
        if self.fname == None:
            return "email does not exist"
        else:
            return "{}.{}@gmail.com".format(self.fname, self.lname)

    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    @fullname.deleter
    def fullname(self):
        print("Name deleted")
        self.fname = None
        self.lname = None


emp1 = Employee("Test", "User")
emp2 = Employee("Test", "User2")
emp3 = Employee("Test", "User3")
