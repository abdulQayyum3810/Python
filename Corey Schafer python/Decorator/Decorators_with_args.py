def prefix_function(prefix):
    def decorator_function(func):
        def wrapper_func(*args, **kwargs):
            print(f"{prefix},Executed before ,{func.__name__}")
            result=func(*args, **kwargs)
            print(f"{prefix}, Executed after ,{func.__name__}")
            return result
        return wrapper_func
    return decorator_function

@prefix_function("TESTING:")
def display_info(name,age):
    print("display_info ran with argument ({}, {})".format(name,age))
    
# behind the scenes
# prefix_function("HELLO")(display_info)("nn",99)