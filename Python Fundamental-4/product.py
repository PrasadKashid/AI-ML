class Product:
    total_product_count = 0
    def __init__(self, name, price):
        self.name  = name
        self.price = price
        Product.total_product_count += 1
        
    @staticmethod
    def calculate_discount(price, discount):
        disconted_price = price - (price * discount / 100)
        print(f"Discounted price is {disconted_price}")
        
    @classmethod
    def get_total_products(cls):
        print("Total number of product is : ",cls.total_product_count)
        
p1 = Product("Laptop", 100000)
p2 = Product("Mobile", 10000)
p3 = Product("pen", 10)

p1.get_total_products()
p1.calculate_discount(p1.price, 10)
