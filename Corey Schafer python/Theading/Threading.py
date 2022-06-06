# synchronous running: executing in sequence
# CPU Bound: tasks that are crunching a lot of numbers and using CPU
# IO Bound: Tasks waiting for input/output to be completed and not using CPU a lot
# (e.g. read/write from file system,other file system opperation, network oppperations, downloading etc)
# Threading is beneficial when our tasks are IO Bound, and if Task is CPU Bound it may slows down the program (by creating and destroying different threads)
# For CPU Bound task multiprocessing is preffered, if we are not sure which to implement (MP,T) try both on subset of our data and see which works faster
# Threading does not run code cocurrently (at the same time) but creates illusion that it is running code cocurrently
# In threading when one opperation is waiting(for IO, or sleeping) other opperation is executed during that time
# All threadings run on same processor
import time, threading
start=time.perf_counter()

def do_something():
    print("Sleeping 1 second")
    time.sleep(1)
    print("Done sleeping")
    
"""t1=threading.Thread(target=do_something)  # Threading objects are created
t2= threading.Thread(target=do_something)

t1.start()  
t2.start()  # Output is unexpected because when our threads runnig do_something function they go to sleep and next code (f string part)  is executed
# and after sleeping is completed next part of the do_something functions is executed to solve this problem us join method as follows
t1.join() # They will ensure that remaing code runs after threads are completed
t2.join()
finish=time.perf_counter()
print(f"Finished in {round(finish-start,2)} seconds")
"""
# creating more threads using for loop

""" threads=[]
for _ in range(10):
    t=threading.Thread(target=do_something)
    t.start()
    threads.append(t)
# cant be done in the same loop because if we apply join after start in the same loop it will complete first thread and then create second 
# and complete and so on (like running code concurrently)
for thread in threads:
    thread.join()

 """


# Passing arguments in the threading

""" def do_something2(seconds):
    print(f"Sleeping {seconds} second(s)")
    time.sleep(seconds)
    print("Done sleeping")
    
threads=[]
for _ in range(10):
    # Pass do_something2 function argument using list
    t=threading.Thread(target=do_something2,args=[1.5])
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()
 """


# FASTER METHOD OF THREADING

import concurrent.futures
def do_something3(seconds):
    print(f"Sleeping {seconds} second(s)")
    time.sleep(seconds)
    return f"Done sleeping {seconds}"

""" with concurrent.futures.ThreadPoolExecutor() as executer:
    f1=executer.submit(do_something3,1)  # Future object is returned, and we can apply different method to future object (like running, done, or getting result)
    f2=executer.submit(do_something3,1)
    print(f1.result())  # result() method waits untill function is executed and returns a value
    print(f2.result())
  """

# Multiple threads using list comprehension, submitting one at a time

""" with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    #secs.reverse()
    results=[executor.submit(do_something3,sec) for sec in secs] # list of future objects, submit is submitting one function at a time
    
    for f in concurrent.futures.as_completed(results):  # Returns iterator object, in the oreder they are completed
        print(f.result())
 """

# Multiple threads using map method, submitting entire list at a time

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    secs.reverse()
    results=executor.map(do_something3,secs) # Will submit all functions at the same time , will return map object having returned values of all functions (As map method gives returned values and submit method returs future objects)
    #print(list(results))
    for result in results:  
        print(result)

finish=time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
