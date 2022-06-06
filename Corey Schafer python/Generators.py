def square_nums(nums):
    for i in nums:  # genertor is using list to be generated (not good)
        yield i*i
my_nums=square_nums([1,2,3,4,5])

print(my_nums.__next__()) # or next(my_nums)

# Same can be done using generator comprehension
my_nums2=(x*x for x in [1,2,3,4,5,6])
print(my_nums2)
print(list(my_nums2))  # Convert generator into a list

# Advantages Examples

import profile
import memory_profiler as mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.perf_counter()
people = people_list(1000000)  # for list analysis
t2 = time.perf_counter()

""" t1 = time.perf_counter()
people = people_generator(1000000)  # for generator analysis
t2 = time.perf_counter() """

print ('Memory (After) : {}Mb'.format(mem_profile.memory_usage()))
print ('Took {} Seconds'.format(t2-t1))