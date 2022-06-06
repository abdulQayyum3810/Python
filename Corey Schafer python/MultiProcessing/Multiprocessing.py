# NOTE: run on ubuntu WSL because multiprocessing is different for windows and linux
# All tasks run at the same time on different processors


import time, multiprocessing
start=time.perf_counter()

""" def do_something():
    print("Sleeping 1 second")
    time.sleep(1)
    print("Done sleeping") """
    
""" 
# Create Process Objects
p1=multiprocessing.Process(target=do_something)
p2=multiprocessing.Process(target=do_something)
# Run process objects
p1.start()
p2.start()

# make sure remaining code runs after both processes finish
p1.join()
p2.join()
 """

# Using for loop to create multiple processes
""" 
processes=[]
for _ in range(10): # we dont have 10 cores but 10 processes, our computer has ability to switch between cores when one is not too busy
    p=multiprocessing.Process(target=do_something)
    p.start()
    # Process objects
    processes.append(p)
for process in processes: # Make sure all processes finish before execution of next code
    process.join()
 """

# Passing arguments of target function

""" def do_something2(seconds):
    print(f"Sleeping {seconds} second(s)")
    time.sleep(seconds)
    print(f"Done sleeping {seconds}s")

processes=[]
for _ in range(10): 
    # Pass args as list (or tuple) containing all args, unlike threading Arguments to multiprocessing process must be able to be serialized using pickle
    # serializing with pickle: converting python object to a format that can be de-constructed and re-constructed in another python script
    p=multiprocessing.Process(target=do_something2,args=[1.5]) 
    p.start()
    # Process objects
    processes.append(p)
for process in processes: # Make sure all processes finish before execution of next code
    process.join() """

#USING FASTER WAY OF MULTIPROCESSING
# It is preffered as it is easy to shift between multiprocessing and threading by just replacing ProcessPoolExecutor with ThreadPoolExecutor, (a lot other benefits as well)
import concurrent.futures

def do_something3(seconds):
    print(f"Sleeping {seconds} second(s)")
    time.sleep(seconds)
    return f"Done sleeping {seconds}s"

""" with concurrent.futures.ProcessPoolExecutor() as executor:
     # Submit() method schedules a function to be executed and returns a future object
     # future object encapsulates execution of our function and allows us to check on it after it has been scheduled (so we can check either it is running, or done and also check the result)
    f1= executor.submit(do_something3,1)
    f2= executor.submit(do_something3,1)
    print(f1.result()) # Grab the return value of our function
    print(f2.result()) """

# Multiple threads using list comprehension, submitting one at a time

""" with concurrent.futures.ProcessPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    # results is list of future objects 
    results=[executor.submit(do_something3,second) for second in secs]
    
# gives an iterator which yields the results of our process as our process complete
for f in concurrent.futures.as_completed(results):
    # as results is list of future objects we have to apply result() method to get the returned value of our function encapsulated in future object
    print(f.result()) """

# Multiple threads using map method, submitting entire list at a time

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    results=executor.map(do_something3,secs)
    
# As results is list of returned values of our function we dont have to apply .result() method (as it is not future object like in previous case)
# All results are in the order they were started (not like as_completed() which orders on the base of completion)
# if any exception raises during Process it will not be raised during process, rather it will be raised when we retrieve the results (same for threading)
for result in results:
    print(result)


finish=time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
