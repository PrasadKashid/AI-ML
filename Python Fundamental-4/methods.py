"""
instance methods

--> 1st compulsory param = self
--> they can access the class and instance attr

class methods

--> 1st param is cls
--> can only access class attributes not instance attributes
--> need to use @classmethod as decorator

static methods
"""

#notes 
"""

object has higher priority than the class 
i.e object can access elements which are part of class and instance attr
but class can only access elements those are class attributes

"""

class Laptop:
    storage_type = "SSD"
    
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
        
    def get_info(self): #instance method
        print(f"Laptop has {self.RAM} and has {self.storage_type} of {self.storage}")
        
    @classmethod # classmethods
    def get_storage_type(cls):
        print(f"Storage type is {cls.storage_type}")
        

laptop1 = Laptop("8GB","512GB")
Laptop.get_storage_type();
laptop1.get_info()