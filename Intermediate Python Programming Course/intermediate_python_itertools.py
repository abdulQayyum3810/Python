#itertools: product,permutations,combinations,accumulate, groupby and infinite iterator(count,cycle,repeat)

#Product
#Returns cartesian product
from itertools import product
from math import comb
list1=[1,2,3,4]
list2=[5]
"""print(list(product(list1,list2,repeat=1)))""" #cartesian product

#Permutations (nPr)
#all possible ordering/permutations of a given iterable
from itertools import permutations
perm=permutations(list1,r=2)
print(list(perm))


#Combination (nCr)
#all possible combinations of an iterable
from itertools import combinations,combinations_with_replacement
comb1=combinations(list1,2)
comb2=combinations_with_replacement(list1,2)
print(list(comb1),'\n',list(comb2))

#accumulate:
#gives accumulated iterable which is achieved using given opperator
from itertools import accumulate
import operator

acc=accumulate(list1,func=operator.mul)
print(list(acc))

#groupby 
#groupby(iterable,function) function defines the criteria on which elements of the iterable are grouped
from itertools import groupby
def smaller_than_3(x):
    return x<3
my_group=groupby(list1,key=smaller_than_3)
#Alternative
"""my_group=groupby(list1,key=lambda x:x<3)"""
for key,value in my_group:
    print(key,list(value))

#infinete iterators (count,cycle,repeat)
from itertools import count, cycle,repeat
#count
for i in count(10,step=2):
    print(i)
    if i==30:
        break
my_count_obj=count(10,3)
print(my_count_obj.__next__())
print(my_count_obj.__next__())
print(my_count_obj.__next__())
print(my_count_obj)
#cycle-->cycles through iterable untill it exhausted and the repeats indefinitely
j=1
for i in cycle(list1):
    print(i)
    j+=1
    if j==9:
        break
#repeat -->see documentation
my_repeat=repeat(list1,5)
print(my_repeat.__dir__)
for i in repeat(list1,4):
    print(i)