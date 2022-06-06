#In FP data and functions are seperated (as not in OOP where attributes and methods belongs to a specific objects)
#In FP we have functions instead of methods, and data
#Pure functions are gives same output to same input if it is run hundredes of times.
#they should not effect the outside world like printing on screen and changing variable outside of its scope
#pure function example
def multipy_by2(li):
    new_list=[]
    for item in li:
        new_list.append(item*2)
    return new_list

#map,filter,zip,reduce funtions

#map
#map function ---.> map(action,iterable data) action is a function which will be implemented on every item of iterable 
#map does not change the iterable data given into its arguments so its a pure function
#it does mapping using the given function
def multiply_by3(item):
    return item*3
my_list=[1,2,3,4]
print(list(map(multiply_by3,my_list)))
print(my_list) #mylist is not effected 

#filter
#filter(action/fuction,iterable data) ---> it will filter data based on the returned value of action(function) and return a filter object
#fuction returns boolean value 

def only_even(num):
    return num%2==0
nums=[1,2,3,4,5,6]
print(list(filter(only_even,nums)))
print(nums) #nums is not changed


#zip
#zip(first iterable,second iterable,...)----> it makes tupples of corresponding elements of all iterables and returns a zip object
#it does not channge the origional data given in arguments
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
str1="pakis"
print(list(zip(list1,list2,str1))) 


#reduce 
#it is part of functool module so import it first
from functools import reduce
#it reduces the iterable to a single value
#reduce(action/function of two arguments,iterable,initial value of accumalator default is 0)
def accumolator(acc,item):
    return acc+item
print(reduce(accumolator,list1,0))


#Lambda Expression
#They are one time anonymus functions
# and they dont have name and dont need to be stored as they are used only once.
# lambda parameters: action on parameters
print("lambda")
add10=lambda x:x+10
print(add10(5))
print(add10(9))
print(list(map(lambda x:x*2,list1)))

#lambda example (square the list items)
print(list(map(lambda x: x**2,list1)))

#lambda example (sort the tuples list based on second item of the tupple)
tuple_list=[(3,4),(4,5),(3,-1),(3,-2)]
tuple_list.sort(key=lambda x:x[1])
print(tuple_list)


#list,tuple,set and dictionary comprehension
#List
my_list1=[num for num in range(0,10)]
print(my_list1)
my_list2=[num for num in range(0,10) if num%2==0]
print(my_list2)

#Sets
my_set1={num for num in range(0,10)}
print(my_set1)
my_set2={num for num in range(0,10) if num%2==0}
print(my_set2)

#Disctionaries
simple_dict={"a":1,"b":2}
my_dict={key:value**3 for key,value in simple_dict.items() if value%2==0}
print(my_dict)