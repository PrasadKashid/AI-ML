#q1

# class BankAccount:
#     def __init__(self, account_number, owner_name, balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.__balance = balance
    
#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Amount {amount} deposited successfully!!")
        
#     def withdraw(self, amount):
#         if(self.__balance > amount):
#             self.__balance -= amount
#             print(f"Amount {amount} withdrawn successfully!!")
#         else:
#             print("Insufficient balance!!")
    
#     def check_balance(self):
#         print("Your current balance is : ", self.__balance)
        
# acc1 = BankAccount(1, "Prasad", 10_00000)
# acc1.check_balance()
# acc1.deposit(12_000)
# acc1.check_balance()
# acc1.withdraw(12_000)
# acc1.check_balance()

# class Book:
#     def __init__(self, title, author, list_of_reviews: list):
#         self.title = title
#         self.author = author
#         self.list_of_reviews = list_of_reviews
        
#     def add_review(self, review):
#         self.list_of_reviews.append(review)
#         print("Review added successfully!!")

#     def count_review(self):
#         print(f"Number of reviews on your book are {len(self.list_of_reviews)}")
    
#     def display_all_review(self):
#         print(f"Your {self.title}'s reviews are : ")
#         for i in self.list_of_reviews:
#             print(i)


# book1 = Book("New", "Prasad",[])
# book1.count_review();
# book1.add_review("It's a great book")
# book1.add_review("Good book")
# book1.count_review();
# book1.display_all_review();

#q3
# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks = marks
        
#     def get_name(self):
#         return self.__name
#     def set_name(self, name):
#         if(name == ""):
#             print("name cannot be empty")
#         else:
#             self.__name = name
    
#     def get_roll_no(self):
#         return self.__roll_no
#     def set_roll_no(self, roll_no):
#         if(roll_no < 0 ):
#             print("Roll No cannot be lesser than 0")
#         elif(roll_no > 100):
#             print("Roll No cannot be greater than 100")
#         else:
#             self.__roll_no = roll_no
        
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self, marks):
#         if(marks < 0):
#             print("Marks cannot be negative")
#         else: self.__marks = marks
        
# student1 = Student("Prasad", 1, 100)

# print("Roll No of student is : ",student1.get_roll_no())
# print("Name of student is : ",student1.get_name())
# print("Marks of student are : ",student1.get_marks())
    
    
# student1.set_name("Ninja")
# student1.set_roll_no(102910)
# student1.set_marks(1000)

#q4 function overriding
# class Shape():
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def calculate_area(self):
#         area = 0
#         radius = float(input("Enter radius to calculate the area "))
#         if(radius > 0):
#             area = 3.14 * radius ** 2
#             print(f"Area of circle is {area}")
#         else:
#             print("Radius cannot be a negative number!!")
            
# class Square(Shape):
#     def calculate_area(self):
#         area = 0
#         side = float(input("Enter side to calculate the area "))
#         if(side > 0):
#             area = side ** 2
#             print(f"Area of square is {area}")
#         else:
#             print("Side cannot be a negative number!!")
            
# class Rectangle(Shape):
#     def calculate_area(self):
#         area = 0
#         length = float(input("Enter length to calculate the area "))
#         breadth = float(input("Enter breadth to calculate the area "))
#         if(length > 0 and breadth > 0):
#             area =length * breadth
#             print(f"Area of rectangle is {area}")
#         else:
#             print("Length or breadth cannot be a negative number!!")

# circle = Circle()
# circle.calculate_area()

# square = Square()
# square.calculate_area()

# rectangle = Rectangle()
# rectangle.calculate_area()

#q5
# class Vehicle():
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand, model)
#         self.seats = seats
        
#     def get_info(self):
#         print(f"Cars details \nBrand : {self.brand} \nModel : {self.model} \nNo of seats : {self.seats}")

# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc
        
#     def get_info(self):
#         print(f"Bike details: \nBrand : {self.brand} \nModel : {self.model} \nEngine CC : {self.engine_cc}")
        
# bike = Bike("Kawasaki","Ninja", 1000)
# bike.get_info()

# car = Car("Honda", "City", 4)
# car.get_info()

#q6
# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self, base_salary):
#         pass

# class Intern(Employee):
#     def calculate_salary(self, base_salary):
#         return base_salary + 0
    
# class FullTimeEmployee(Employee):
#     def calculate_salary(self, base_salary):
#         return base_salary + 5000

# class ContractEmployee(Employee):
#     def calculate_salary(self, base_salary):
#         return base_salary + 1000
    

# intern = Intern()
# print("Intern's salary is : ",intern.calculate_salary(1000))
        
# full_time_emp = FullTimeEmployee()
# print("Full time employee's salary is : ",full_time_emp.calculate_salary(100000))

# contract_employee = ContractEmployee()
# print("Contract based employee's salary is : ",contract_employee.calculate_salary(10000))

#q8
# class Player():
#     player_count = 0
    
#     def __init__(self):
#         Player.player_count += 1
    
#     def create_player(self, name, level):
#         print("Player created successfully")
    
#     @classmethod
#     def players_count(cls):
#         print("Players count : ", cls.player_count)
        
    
# player1 = Player()
# player2 = Player()
# player3 = Player()
# player4 = Player()
# player1.create_player("Prasad", 100)
# Player.players_count()

"""

"""


# q9
class Herbivore:
    def __init__(self):
        print("Herbivore init")
        super().__init__()

class Carnivore:
    def __init__(self):
        print("Carnivore init")
        super().__init__()

class Omnivore:
    def __init__(self):
        print("Omnivore init")
        super().__init__()
        
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self):
        print("Bear init")
        super().__init__()

bear = Bear()

        