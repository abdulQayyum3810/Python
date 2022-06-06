#Errors(syntax) and exceptions (logical)
#03116817206
x=-5

"""if x<0:
    raise Exception("x should be positive") #raise an error
"""
#Alternative to raise an error
#assert(x>=0), "x should be positive" #Error is raised if condition is False
try:
    5/0
except Exception as e: #get any type of exception catched and stored to the variable e
    print(e)

#multiple except statements can also be added but only  one statement will be executed which one 
#matches first
try:
    5/1
    a=5+"18"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else: #runs if none of above exception accures
    print("everything is fine")
finally:#Always gets executed whether exception occures or not
    print("cleaning up")

# Defining own errors
class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self,message,value) -> None:
        self.message=message
        self.value=value
def test_func(x):
    if x>100:
        raise ValueTooHighError("value is too high")
    if x<5:
        raise ValueTooSmallError("Value is too small",x)
try:
    test_func(0)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(f"{e.message},x={e.value}")