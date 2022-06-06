# when we run python file before doing anything python sets some special variables 
# one of them is __name__ >> it is equal to __main__ when a file is run directly
# if file is run from other file (by importing i.e. when we import some module python runs that module file)
# then __name__ = module_name now we check whether file is run directly or from other file and make some functions run
# according to that

print("This line will run always whether file is ran directly or imported")

# Recommended
def test():
    pass


def main():
    pass # do something


  # funtion main() and test() will only run if we are running this file directly (not importing it), to run 
  # these functions from other file (by importing this file into other file) use First_module.main() 
  # and First_module.test()
  
if __name__=="__main__":
    # Benefit of this way of writting code is if we still want run these function in other files then it is 
    # still possible using First_module.main() and First_module.main()
    main() 
    test()     
    
    
# Other scenerio
if __name__=="__main__":
    print("This block will if file is run directly")
    main()     
else:
    print("this block will run if this file is run by import")
    #do something