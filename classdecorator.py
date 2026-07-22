def class_decorator(cls):
    class NewClass(cls):
        def show(self):
            print("Decorator Added")
            super().show()
    return NewClass

@class_decorator
class Demo:
    def show(self):
        print("Original Class")

obj = Demo()
obj.show()
