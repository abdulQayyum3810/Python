def add_employee(emp,emp_list=[]):
    emp_list.append(emp)
    print(emp_list)
    
    
def add_employee_fixed(emp,emp_list=None):
    if emp_list is None:
        emp_list=[]
    emp_list.append(emp)
    print(emp_list)

# Now if we dont pass emp_list we expect emp_list to be created every time function is called but output is unexpected 
# The reason is that python  evaluates the default parameters once at the time when it creates the function (eg. instead of creating emp_list everytime we run the funciton)
# In our case default emp_list will be created once at the time of function creation and it will be set to emp_list every time function is called with default parameter emp_list
# Now if emp_list is changed (as it is mutable) then on next function call changed value will be set to default parameter
print(add_employee.__defaults__)   # gives defaul parameter values of function
add_employee("Corey")
print(add_employee.__defaults__)  
add_employee("Jhon")  # appended to the previous list
print(add_employee.__defaults__) 
add_employee("helly")
print(add_employee.__defaults__) 


# FIXED EMPLOYEE FUNCTION
# Defaul values are always None (immutable) so whenever fuction is called the same value is set to default parameters
print("FIXED EMPLOYEE FUNCTION")
print(add_employee_fixed.__defaults__)
add_employee_fixed("Corey")
print(add_employee_fixed.__defaults__)  
add_employee_fixed("Jhon") 
print(add_employee_fixed.__defaults__) 
add_employee_fixed("helly")
print(add_employee_fixed.__defaults__) 



# Datetime example
from datetime import datetime
from time import sleep

def display_time(time_to_print=datetime.now()):
    print(time_to_print.strftime("%B %d,%Y %H:%M:%S"))

print(display_time.__defaults__)
display_time()
sleep(1)
display_time()  # Default value is not changed because it was evaluated at time of function creation and then same value is set to dafault parameter every time
sleep(1)
display_time()
sleep(1)

def display_time_fixed(time_to_print=None):
    if time_to_print is None:
        time_to_print=datetime.now()
    print(time_to_print.strftime("%B %d,%Y %H:%M:%S"))

print("FIXED DATETIME")
print(display_time_fixed.__defaults__)
display_time_fixed()
sleep(1)
display_time_fixed() 
sleep(1)
display_time_fixed()
sleep(1)