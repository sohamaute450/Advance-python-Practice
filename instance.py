class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

        def display(self):
            print("name,",self.name)
            print("age,",self.age)

#creating object
s1=student("Rahul", 20)
s2=student("Monu",19) 

#displaying information of each object
s1.display()
print()
s2.display()
