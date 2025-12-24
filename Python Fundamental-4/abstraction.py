from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Cat(Animal):
    def make_sound(self):
        print("Meow")
        
class Lion(Animal):
    def make_sound(self):
        print("Roar")

cat = Cat()
cat.make_sound()
lion = Lion()
lion.make_sound()