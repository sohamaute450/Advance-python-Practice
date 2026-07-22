class Student:
   
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

   
    def display(self):
        print("Student Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    
    def result(self):
        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")



student1 = Student("Soham", 101, 85)
student2 = Student("Nahush", 102, 35)


student1.display()
student1.result()
print("\n")
student2.display()
student2.result()
