# Closure helps to take advantage of first class functions and returns inner functions 
# which remmebers its free variable when its was created
#  03437523328
# DECORATORS:
# Takes a function as argument add some functionality to it and returns another function
# Basics are in D:\Education\UET\CS\Python\CoderCat\CoderCat Code\Decorators.py

# Functions and Classes as decorators
# Implementing same decorator using function and class

from time import sleep, time


def decorator_function(original_function):
    def wraper_func(*args,**kwargs):
        print(f"Wrapper ran this statement berfor {original_function.__name__}")
        return original_function(*args,**kwargs)
    return wraper_func

class DecoratorClass(object):
    def __init__(self,original_function) -> None:
        self.original_function=original_function
    def __call__(self, *args, **kwargs): #  Same as wrapper function
        print(f"call method ran this statement berfor {self.original_function.__name__}")
        return self.original_function(*args,**kwargs)


@decorator_function
def display_info(name,age):
    print(f"display_info ran with argument ({name} , {age})")
# display_info=wraper_func("AQ", 23)
display_info("AQ", 23)

@DecoratorClass
def display_info(name,age):
    print(f"display_info ran with argument ({name} , {age})")
# display_info=wraper_func("AQ", 23)
display_info("AQ", 23)

# PRACTICAL EXAMPLES
""" 
def my_logger(original_function):
    import logging
    logging.basicConfig(filename="{}.log".format(original_function.__name__),level=logging.INFO)
    def wrapper_func(*args,**kwargs):
        logging.info(f"Ran with args: {args} and kwargs: {kwargs}")
        return original_function(*args,**kwargs)
    return wrapper_func

def my_timer(func):
    import time
    
    def wrape_func(*args,**kwargs):
        t1=time.time()
        result=func(*args,**kwargs)
        t2=time.time()
        print(f"{func.__name__} took {t2-t1}  second(s)")
        return result
    return wrape_func

    

# Using multiple decorators on same function
print("\n\nMULTIPLE DECORATORS with issues")
 
@my_logger
@my_timer
def display_info2(name,age):
    sleep(1)
    print(f"display_info ran with argument ({name} , {age})")
# display_info=wraper_func("AQ", 23)
display_info2("AQ", 23) """

# in background
""" display_info2=my_logger(my_timer(display_info2)) # display_info2=logger(wrape_func)
display_info2("AQ2",23) """

# The output was not as we expected (wrape_func was logged instead of display_info2)
# To solve this problem use func tool
from functools import wraps
def my_logger_fixed(original_function):
    import logging
    logging.basicConfig(filename="{}.log".format(original_function.__name__),level=logging.INFO)
    
    @wraps(original_function)  # Fixed issue
    def wrapper_func(*args,**kwargs):
        logging.info(f"Ran with args: {args} and kwargs: {kwargs}")
        return original_function(*args,**kwargs)
    return wrapper_func

def my_timer_fixed(func):
    import time
    
    @wraps(func)  # Fixed issue
    def wrape_func(*args,**kwargs):
        t1=time.time()
        result=func(*args,**kwargs)
        t2=time.time()
        print(f"{func.__name__} took {t2-t1}  second(s)")
        return result
    return wrape_func

    

# Using multiple decorators on same function
print("\n\nMULTIPLE DECORATORS solved")
 
@my_logger_fixed
@my_timer_fixed
def display_info3(name,age):
    sleep(1)
    print(f"display_info3 ran with argument ({name} , {age})")
    
display_info3("Display_info fixed", 22)

