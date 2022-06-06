# Module is a python file and Package is folder contain modules(python files)
# modules contain classes and functions and other python code

import utility  # importing module we created
# on import pycache files will be generated which are compiled version of imported module
# next time we run our main file pycache files of each module will be imported instead of original module.py files
# if module file is changed then its pycache file will also be changed
print(utility)  # path of utility module will be printed
# if we have package inside package we can reach to our desired module using . notation
# from package.package import module now module is imported to use its function use
# module.function (or other attributes)
print(utility.divide(2, 3))  # using function in our module


import Shopping.shopping_cart
print(Shopping.shopping_cart.buy("apple"))

print(__name__)  # Name of the file or module , the file we are current running is called __main__
# other file/module which are imported have same name as their .py file name
if __name__ == "__main__":  # ensures to run code inside it only if we are in main file because file can also be imported and ran by interpreter at time of importing
    print("Please run if we are in main file")

# Built in modules
from random import shuffle as sh  # Using Aliases
my_list=[1,2,3,4,5]
sh(my_list)
print(my_list)

import sys
#if we run file from terminal and give some arguments these arguments can be accessed using sys.argv
# python3 file.py arg1 arg2 arg3
# access these args in file as arg1=sys.argv[1], arg2=sys.agrv[2]


# PACKAGES
# Search first "python csv builtin" replace 'python csv' with 'required package'
# Standard Packages: https://docs.python.org/3/py-modindex.html
# Third Party Packages: pypi.org
# pip install package==version(0.6.7)
# pip list : list all packages installed by pip

# VERSION
# 5.5.6 Breaking Changes.new release (added features).bugfixes



#USEFULL STANDARD PACKAGES
# collections : Counters, defaultdict
# datetime:
# time:
# Array