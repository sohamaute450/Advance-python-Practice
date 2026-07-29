class number:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <=5:
            x=self.num
        self.num +=1
        return x
    
        raise StopIteration
#create object
obj= number()

for i in obj:
    print(i)
      
