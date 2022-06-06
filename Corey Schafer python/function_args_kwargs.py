#rule is positional args, args and kwargs
#when defining a function
# *arbitrary no of positional args
# ** arbitrary no of kwargs

#Meanings when calling the functions
# * unpacks the lists and tuples
# ** unpacks the dictionary

def my_function(a,b,c,*args,**kwargs):
    print("a=",a,"b=",b,"c=",c)
    print("args",args)
    print("kwargs",kwargs)
args1=(5,4,3,4)
kwargs1={"a":4,"b":3,"c":5}
kwargs2={"d":4,"e":3,"f":5}
my_function(**kwargs1,p="f") #keyword args can follow kwargs unpacking but
# args cant follow kwargs unpacking like my_function(**kwargs,5,6,7)
my_function(*args1,**kwargs2)
