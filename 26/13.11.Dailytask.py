
#Data Abstracion:-  used to hide unnecessary information and display only necessary information to the users interacting.

#1. Abstract Classes: These are classes that cannot be instantiated directly and may contain abstract methods that must be implemented by subclasses. You can create abstract classes using the abc (Abstract Base Class) module.
 
 
#2. Abstract Methods: Methods in an abstract class that have no implementation. They must be overridden in any subclass.


from abc import ABC, abstractmethod

# Create Abstract base class
class Bike(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
         
    @abstractmethod
    def printDetails(self): 
        pass
  
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Bike stopped")

# Create a child class
class Hatchback(Bike):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def automatic(self):
        print("Not having this feature")

# Create a child class
class R15(Bike):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def automatic(self):
        print("Available")

# Create an instance of the Hatchback class
Bike1 = Hatchback("Yamaha", "ZMR", "2023")

# Call methods
Bike1.printDetails()
Bike1.accelerate()
Bike1.automatic() 