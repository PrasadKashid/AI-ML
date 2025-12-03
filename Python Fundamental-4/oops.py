class Student():
    
    def __init__(self, name :any = None, cgpa: any = None):
        self.name = name
        self.cgpa = cgpa
    
    def get_cgpa(self):
        return self.cgpa
        
stu1 = Student("Nisha", 9.55)
print(f"{stu1.name}'s CGPA is {stu1.get_cgpa()}")

