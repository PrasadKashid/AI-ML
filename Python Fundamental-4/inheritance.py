"""
Resuing attr and methods from a Parent(base) class
"""

# class Employee:
#     start_time = "10AM"
#     end_time = "6PM"
    
#     def change_time(self, new_start_time):
#         self.start_time = new_start_time
        

# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject
    
# class Admin(Employee):
#     def __init__(self, role):
#         self.role = role
    
# t1 = Teacher("Maths")
# t1.change_time("9AM")
# # print(t1.subject, t1.start_time, t1.end_time)

# staff1 = Admin("Teacher")
# print(staff1.role,staff1.start_time)


# class Accountant(Admin):
#     def __init__(self, salary, role):
#         super().__init__(role)
#         self.salary = salary

class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary,gpa, name):
        super().__init__( salary)  #no need to call self
        Student.__init__(self,gpa) # need to call self
        self.name = name
        
ta1 = TA(15_0000, 9.34, "Prasad")
print(ta1.name, ta1.gpa, ta1.salary)
        