# First Class Functions: Support all opperations generally available to other entities 
# (typically these opperations includes passed as argument, assigned to variable, returned by another function)


def square(x):
    return x**2

f= square(5)  # Returned value is assigned to f
j=square   # Now j also points to same square function in memory if we delete square funtion it will still be in the memory as j is still pointing to it.
print(square)
print(j)

#Higher Order Function is defined as
#1. it is accepting function as argument
#2. it returns a function


# Passing as argument
def my_map(func, args_list):
    result=[]
    for arg in args_list:
        result.append(func(arg))
    return result

cubes=my_map(lambda x: x**3, [1,2,3,4,5,6])
print("Cubes",cubes)

# Returning function
def logger(msg):
    def log_msg():
        print("Log, ",msg)
    return log_msg

log_hi=logger("Hi") # log_hi equal to log_msg funtion and also remembers msg which is passed to logger function
log_hi()
print(log_hi)  # print where log_hi variable points
print(log_hi.__name__)  # print name of the function to which log_hi points

# Returning function practical example

def html_tag(tag):
    def wrap_text(msg):
        print("<{0}> {1} </{0}>".format(tag,msg)) # tag is free variable as accessed but not defined in this block
    return wrap_text
print_h1=html_tag("h1") # Now treat print_h1 as wrap_text funtion but it remmebers the tag variable passed to html_tag function using closure
print_h1("The test headline")
print_h1("Another Headline") # Basically we are calling wrap_text function with remembered tag passed to html_tag function using closure

print_p=html_tag("p")
print_p("Test Paragraph")
