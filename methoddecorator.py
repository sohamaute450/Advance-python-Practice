def method_decorator(func):
    def wrapper(self):
        print("Before Method")
        func(self)
        print("After Method")
    return wrapper

class Student:
    @method_decorator
    def display(self):
        print("Student Method")

obj = Student()
obj.display()
