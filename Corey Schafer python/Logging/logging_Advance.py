import logging
# if logger is not set for logging_employee_class following will run the logging_employee_class and as we know in that file we have logs which will be 
# created but sample.log  in this file will not be created because when logging_employee_class is run employee.log and all log settings 
# are configured as root logger (because it ran first) and we share the same root
# To get new handler for logging_employee_class we have to create new handler in logging_employee_class
import logging_employee_class 

# setting logger for our this scriptlogger

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)  # Setting level for our new logger but level for file handlers can also be set
file_handler = logging.FileHandler("sample.log")  # Create file handler
file_handler.setLevel(logging.ERROR)  # Setting level for file handler
# Getting a formator object for our handler (file or stream or any other handler)
formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)  # Setting format for our file handler
logger.addHandler(file_handler)  # Add file handler to our logger

stream_handler=logging.StreamHandler()  # Getting stream handler it will have the level of our logger (DEBUG)
# Multiple handler can be adder to logger
stream_handler.setFormatter(formatter)  # Setting same formatter for stream handler (different formatter can also be set)
logger.addHandler(stream_handler)  # Adding to logger


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multipy(x, y):
    return x*y


def divide(x, y):
    try:
        result=x/y
    except ZeroDivisionError:
        # Handled by file handler sample.log
        """ logger.error("Tried to divide by zero") """ 
        logger.exception("Tried to divide by zero")  # its better as it gives traceback also
        
    else:
        return result

num_1 = 50
num_2 = 0


# following logs are not being shared to 
add_result = add(num_1, num_2)
logger.debug(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = subtract(num_1, num_2)
logger.debug(f"Subtract: {num_1} + {num_2} = {sub_result}")

mul_result = multipy(num_1, num_2)
logger.debug(f"Multiply: {num_1} + {num_2} = {mul_result}")

div_result = divide(num_1, num_2)
logger.debug(f"Divide: {num_1} + {num_2} = {div_result}")
