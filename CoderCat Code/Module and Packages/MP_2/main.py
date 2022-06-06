# Module is a python file and Package is folder contain modules(python files)
# modules contain classes and functions and other python code
# when module is imported it is run that how python creates fuctions and variables present in module

# if we have package inside package we can reach to our desired module using . notation
# from package.package import module now module is imported to use its function use
# module.function (or other attributes)


# good practice is import module and access its  attributes (fuctions/variable/classses) with dot (module.attribute) in this way 
# they will not  overwrite our functions/variable/class insideo our main file
# if we want to import specific attributes of a module then import them explicitly (from module import attribute_1, attribute_2) instead of 
# (from module import * ), module will still run on import but we will have access to only specified attiributes
# now dont assign same attribute_name for any attribute in our main file

import utility  # importing module we created
# on import pycache files will be generated which are compiled version of imported modules
# next time we run our main file pycache files of each module will be imported instead of original module.py files
# if module file is changed then its pycache file will also be changed
print(utility)  # path of utility module will be printed

print(utility.divide(2, 3))  # using function in our module


import Shopping.shopping_cart
print(Shopping.shopping_cart.buy("apple"))

print(__name__)  # Name of the file or module , the file we are current running is called __main__
# other file/module which are imported have same name as their .py file name


if __name__ == "__main__":  # ensures to run code inside it only if we are in main file because file can also be imported and ran by interpreter at time of importing
    print("Please run if we are in main file")


# if we run file from terminal and give some arguments these arguments can be accessed using sys.argv
# python3 file.py arg1 arg2 arg3
# access these args in file as arg1=sys.argv[1], arg2=sys.agrv[2]
import sys
# directories hierarchy for searching imported packages
print(sys.path)
 # Adding directory to system path if our packages are in our customized directory(Not recommended way recommended is 
 # adding environment variables)
 # Add environment variables: (linux:https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)
 # Add environment variables: (windows: Add PYTHONPATH as environment variable, use ; as delimeter between paths to add more
 # than one path to same variable)
""" sys.path.append("path to packages for seaching") """
 

 






# PACKAGES
# Search first "python csv builtin" replace 'python csv' with 'required package'
# Standard Packages: https://docs.python.org/3/py-modindex.html
# Third Party Packages: https://pypi.org
# pip install package==version(0.6.7)
# pip list : list all packages installed by pip


# VERSION Reading
# 5.5.6 Breaking Changes.new release (added features).bugfixes



#USEFULL STANDARD PACKAGES
# collections : Counters, defaultdict
# datetime:
# time:
# Array, math, calender, os, 