# FORMAL DEFINTION:
#  Closure is a, Record: which stores the function together its environment, mapping: associating each free 
# variable of the funtion with its value/location to which the name was bound when function closure was created
# It allows the functions to access variables through the closure's reference to them, even when the functions 
# are invoked outside of their scopes

# SIMPLE DEFINITION:
# In simple words closure is  inner function that remembers and has access to variables in the local 
# scope in which it was create even outer fuction has finish exection (even outer function is deleted)
# ( to remember closure closes over the free variable in their environment)

# Free Variable: A variable which is accessed in a block (scope) but not defined in that 
# block/scope (defined in higher/other block) like messege in following example

def outer_fun():
    message="Hi"
    def inner_fun():
        print(message)
    return inner_fun

my_msg=outer_fun()
my_msg()
print(my_msg)  # print where my_msg variable points
print(my_msg.__name__)  # print name of the function to which my_msg points
del outer_fun
my_msg()  # we still have access to message variable even outer_funtion in which it was defined is deleted


# Outer function and inner function with arguments

def html_tag(tag):
    def wrap_text(msg):
        print("<{0}> {1} </{0}>".format(tag,msg)) # tag is free variable as accessed but not defined in this block
    return wrap_text
print_h1=html_tag("h1") # print_h1 is points to wrap_text function but closure remembers the free variable tag (tag=h1) when print_h1 was created
print_h1("The test headline") # wrap_text function is being invoked outside of its scope (through pointing variable print_h1) and closure remembers all free varible values associated to wrap_text fuction when print_h1 was created

print_p=html_tag("p")  # This time free variable stored in closure has value tag=p
print_p("Test Paragraph")

html_tag("h2")("This is h2 tag")  # calling another way

# Advance example

import logging
logging.basicConfig(filename="example.log",level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info("Runnig '{}' with arguments {}".format(func.__name__,args))
        print(func(*args))
    return log_func

def add_nums(x,y):
    return x+y
def sub_nums(x,y):
    return x-y

add_logger=logger(add_nums) # add_logger points to inner function (log_fun) and closure will remember the free variable (func=add_nums)
sub_logger=logger(sub_nums) 

add_logger(3,4)  # log_runs with (func=add stored in closure)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20,10)

print(sub_logger)
