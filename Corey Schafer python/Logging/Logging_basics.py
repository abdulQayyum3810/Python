import logging

# There are five standard logging levels
# DEBUG: Detailed information useable for debugging
# INFO: Confirmation that everything worked as expected
# WARNING: Indication that something unexpected happened (or expected to happen in near future e.g disk space low)
# but software is still working as expected
# ERROR: Due to some serious problems software has not been able to perform some functions
# CRITICAL: A serious error, indicating that software itself may not able to continue running
# By default level is WARNING so it will capture warnings and anything above (WARNING,ERROR, CRITTICAL)

# if file name is set then logging information will go to file otherwise to console
# All levels above the set level will be captured
# for format options https://docs.python.org/3/library/logging.html#logrecord-attributes

logging.basicConfig(filename="logging_basics_test.log", level=logging.DEBUG,
                    format="%(asctime)s: %(levelname)s: %(message)s")


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multipy(x, y):
    return x*y


def divide(x, y):
    return x/y


num_1 = 50
num_2 = 5

add_result = add(num_1, num_2)
logging.debug(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = subtract(num_1, num_2)
logging.debug(f"Subtract: {num_1} + {num_2} = {sub_result}")

mul_result = multipy(num_1, num_2)
logging.debug(f"Multiply: {num_1} + {num_2} = {mul_result}")

div_result = divide(num_1, num_2)
logging.debug(f"Divide: {num_1} + {num_2} = {div_result}")
