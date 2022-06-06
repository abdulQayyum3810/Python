#Functions are first class objects in python i.e. they can be called as variables, passed in as arguments, returned from other functions and available to other objects etc
def hello_func():
    return "hello"

greeting=hello_func() # returned value will be stored in the greeting variable
print(greeting)
greet=hello_func #now greet is also a function and can be callead as function which points to the same function in memory (i.e. hello_func)
# if hello_func is deleted (del hello_func) but it will not be deleted in memory as greet is still pointing to that function in memory and can be called using greet()
#get function memory location
print(greet)
print(hello_func)
del hello_func
print(greet)

#Higher Order Function is defined as
#1. it is accepting function as argument
#2. it returns a function

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>DECORATORS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Decorators syntax for defining 
def my_decorator(func): #main decorator which is HOC and accepts a function
    def wrap_func():#define wrapper function
        print("*********")
        func() #call functin passed and add functionaliy
        print("*********")
    return wrap_func #return wrapper function


#Using a decorator
@my_decorator #  #in background hello=my_decrator(hello)
def hello():
    print("hello")
#  now wrapper function is executed instead of hello i.e. hello function now has extra functionality
# which is given by wrapper function of my_decorator
hello()

@my_decorator #by using this single line, wrapper function's functionality can be added to any function
def bye():
    print("bye bye")
bye()


#Working behind the scenes of decorators
#my_decorator is called with hello function in argument 
my_decorator(hello)() #it returns wrap function which is called with outer brackets



#Handling Arguments
def my_decorator2(func):
    def wrap_func(x,y):
        print("*********")
        func(x,y) 
        print("*********")
    return wrap_func

@my_decorator2 
def hello2(greetings,smile):
    print(greetings,smile)
    
# now hello2=my_decorator(hello2) >>> hello2=wrap_func() 
# if we pass we pass arguments to hello2(x,y) they will be passed to wrap_func as hello2=wrap_func
# to handle these arguments wrap_function must accept arguments
hello2("hello i'm hello2","smilling") 
#in the background
a=my_decorator2(hello2) #decorator function  takes hello2 as argument pass it to wrapper function and returns wrapper function which is ready to be called using a
a("hello i'm hello2 called second time","smilling") # now a is pointing to  wrapper function which takes the argument and pass it to inner func (func=hello2 remembers by closure)


#Handling Arbitrary number of arguments
#it makes decorators flexible to be used on any function which have any number of args and kwargs
def my_decorator3(func): 
    def wrap_func(*args,**kwargs): #pass as many args as we want
        print("*********")
        func(*args,**kwargs) #unpack the args and kw args
        print("*********")
    return wrap_func 
@my_decorator3
def hello3(greetings,smile):
    print(greetings,smile)

hello3("hello i'm hello3","smilling") #hello functions is passed to the decorator function which returned wrapper function 
# wrapper function takes args and kwargs and the they are upacked in the by hello3 function


#Application example
from time import time
def performance(func):
    def wrap_func(*args,**kwargs):
        t1=time()
        result=func(*args,**kwargs) # wrapper function will run the passed function (which is free variable and remembered by closure) and stores it result to return
        t2=time()
        print(f"it took {t2-t1} s")
        return result 
    return wrap_func
@performance # now this decorator can be used for any function to measure its performance
def long_run():
    for i in range(10000000):
       j= i*5
    return j
print(long_run())