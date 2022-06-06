#simple example

#except block will handle if any type of exception occures in the try block
#else block will be executed if no error happens (it is adjcent to the except block)

"""while True:
    try:
        age=int(input("Enter your age: "))
        print(age)
    except:
        print("Please enter a number")
    else:
        print("Thank You")
        break"""

#multiple error blocks
"""while True:
    try:
        age=int(input("Enter your age: "))
        print(age)
    #if one except block is executed others will be omitted like in if elif statement
    except ValueError as ve:
        print("Please enter a number",ve)
    except ZeroDivisionError:
        print("please enter age higher than 0")
    else:
        print("Thank You")
        break"""

#multiple errors in one except block
while True:
    try:
        age=int(input("Enter your age: "))
        print(17/age)
        
    except (ValueError,ZeroDivisionError) as err:
        print (err)
    else:
        print("Thank You")
        break
    #finally statement runs always no matter what (enven if loop breaks before finally, continue statement)
    finally:
        print("finally")

#defining and raising our own errors