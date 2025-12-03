class Student:
    college_name = "Terna college of engineering" #class attributes
    PI = 3.1
    
    def __init__(self, name, cgpa):
        self.name = name            #instance attr
        self.cgpa = cgpa
        self.PI = 3.14
    
    
stu1 = Student("Prasad", 9.2)
print(Student.PI) 
print(stu1.PI) # this access the instance attr 

"""
Instance attr has higher priority than class attr
"""