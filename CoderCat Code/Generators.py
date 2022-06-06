# Iterable objects uses __iter__ method

#GENERATORS
#Allows us to generate sequence of values over time
#Generators are also iterable
#they hold only one item in the memory at a time
#function is paused after an item is yeilded from generator until the next is requested (using next method())
#when we reached at the end of the sequence StopIteration Exception is raised
#range() is a generator


#Generators syntax
def generator_function(num):
    for i in range(num):
        yield i  #unlike return (which exit the function) yield pauses the function and remembers the las status

g=generator_function(100)
g2=generator_function(10)
print(next(g))
print(next(g))
print(next(g2))
print(next(g))
print(next(g2))
print(next(g))

#efficiency exmple
from time import time
def performance(func):
    def wrap_func(*args,**kwargs):
        t1=time()
        result=func(*args,**kwargs)
        t2=time()
        print(f"{func.__name__} took {t2-t1} s")
        return result 
    return wrap_func
@performance 
def long_time1():
    print("long_time1 (generator")
    for i in range(1000):
      i*5

@performance 
def long_time2():
    print("long_time2 (list)")
    for i in list(range(1000)):
       i*5

long_time1()
long_time2()

#for loop working in background
def special_for(iterable):
    iterator=iter(iterable) #gives extra features like next() to be used on iterable
    while True:
        try:
            print(iterator) #to see objects memory location (will be at same location)
            print(next(iterator))
        except StopIteration:
            break
    return
print("\n Special for loop")
special_for([1,2,3,4,5,6])

#Creating our own ranges

class MyGen():
    def __init__(self,first,last,n=1) -> None:
        self.first=first
        self.last=last
        self.n=n #increment for each object
        self.current=self.first #initialize current location
    #compulsory special methods to be defined to make our own generator
    def __iter__(self):
        return self
    def __next__(self): #required by for loop
        if self.current<self.last:
            num=self.current
            self.current+=self.n
            return num
        raise StopIteration

gen=MyGen(100,110)
for i in gen:
    print(gen) #get memory location
    print(i)

#Fibnoci Series using Generators

def fibnoci_series(terms):
    a=0
    b=1
    for i in range(terms):
        yield a
        a,b=b, a+b
        
#Looping through fibnoci Series generator
for i in fibnoci_series(10):
    print(i)