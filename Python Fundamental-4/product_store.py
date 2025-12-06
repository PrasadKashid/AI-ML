class Product:
    total_prod = 0
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_prod += 1
    
    def get_info(self): #instance method
        print(f"Price of {self.name} is Rs.{self.price}")
        
    @classmethod
    def get_count(cls):
        print(f"Total count of product is {cls.total_prod}")
        
    @staticmethod
    def get_discount(price,discount):
        final_price = price - (price * discount / 100)
        print(f"Product's final price is {final_price}")
        
    
p1 = Product("Phone", 28_000)
p2 = Product("Laptop", 50_000)
p3 = Product("Pen", 50)

p1.get_info()
p2.get_info()
p3.get_info()

Product.get_count();
Product.get_discount(910_1000, 15)