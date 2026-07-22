# Decorator function
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

# Using the decorator
@my_decorator
def greet():
    print("Hello, World!")

# Calling the function
greet()
