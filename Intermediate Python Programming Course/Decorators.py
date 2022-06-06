#Decorators are higher order functions and takes other functions as argument and extends the behaviour of the function
#syntax
"""@decorator_name
    def function_name():
    pass"""

#python functions are first class object it means like other objects they can be passed as an argument
# , returned, and defined in other functions
def start_end_decorator(func):
    def wrapper():
        print("Start") #Added functionality before func
        func()
        print("End") #Added functionality after func
    return wrapper

"""def print_name():
    print("Alex")
print_name=start_end_decorator(print_name)"""

#Alternative(Using decorator)
@start_end_decorator
def print_name():
    print("Alex")

print_name()
print("\n\n Function with arguments")
#functions with arguments
from functools import wraps
from unittest import result
def start_end_decorator2(func):
    @wraps(func)   #prserve the identity of the original function
    def wrapper(*args,**kwargs):
        print("Start") #Added functionality before func
        result=func(*args,**kwargs)
        print("End") #Added functionality after func
        return result
    return wrapper

@start_end_decorator2
def add10(x):
    return x+10

a=add10(4)
print(a)
print(add10.__name__) #check name of the function without line 30 it becomes wrapper() and add10 loses its identity

#Decorators with arguments
def repeat(num_times):
    def repeat_decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result=func(*args,**kwargs)
            return result
        return wrapper
    return repeat_decorator



@repeat(num_times=5)
def greet(name):
    print(f"Welcome {name}")

greet("Alex")


#Nested Decorators later 