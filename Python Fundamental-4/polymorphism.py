# function overriding

class Employee:
    def get_designation(self):
        print("Designation = Employeee")
        
class Teacher(Employee):
    def get_designation(self):
        # print("Designation = Teacher")
        super().get_designation()

teacher = Teacher()
# teacher.get_designation()

class Student:
    def get_name(self):
        print("Student")
class Clerk:
    def get_name(self):
        print("CLerk")

s1 = Student()
s1.get_name()

c1 = Clerk()
c1.get_name()
