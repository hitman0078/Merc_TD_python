from abc import ABC, abstractmethod


# 1. The Abstract Class (The strict blueprint)
class Vehicle(ABC):

    """Vehicle class"""
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def drive(self):

        """We leave this empty because every vehicle drives differently"""


# 2. Subclasses (Must implement the abstract methods)
class PetrolCar(Vehicle):

    """Petrol car class"""
    def drive(self):

        """Drive function taken from abstract class above - polymorphism"""
        print(f"{self.brand} is burning fuel to move.")


class ElectricCar(Vehicle):

    """Electric vehicle"""
    def drive(self):

        """Drive function taken from abstract class above - polymorphism"""
        print(f"{self.brand} is using battery power to move.")
# --- The "Strictness" Test ---

# try_vehicle = Vehicle("Generic")
# ^ This would throw an ERROR: "Can't instantiate abstract class Vehicle"


my_petrol = PetrolCar("Toyota")
my_petrol.drive()