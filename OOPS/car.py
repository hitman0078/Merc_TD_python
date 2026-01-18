class Car:
    
    def __init__(self, brand: str, color: str = "unknown"):
        
        self.brand = brand
        self.color = color

    def hello(self):
        """
        Prints a greeting message, identifying the class it's called from.
        """
        print(f"Hello from {self.__class__.__name__}")

    def drive(self):
        
        print(f"The {self.color} {self.brand}")


class ElectricCar(Car):
    """
    ElectricCar
    """
    def __init__(self, brand: str,
                 color: str = "unknown",
                 battery_capacity_kwh: int = 75):
        
        super().__init__(brand, color)
        self.battery_capacity_kwh = battery_capacity_kwh

    def hello(self):
        """
        Prints a greeting message, identifying the class it's called from.
        """
        print(f"Hello from {self.__class__.__name__}")

    def drive(self):
        
        print(f"The {self.color} {self.brand}: ... (Silent electric hum)")


class Truck(Car):
    """
    Truck
    """
    def __init__(self, brand: str,
                 color: str = "unknown",
                 payload_capacity_kg: int = 5000):
        
        super().__init__(brand, color)
        self.payload_capacity_kg = payload_capacity_kg

    def hello(self):
        """
        Prints a greeting message, identifying the class it's called from.
        """
        print(f"Hello from {self.__class__.__name__} Designer")

    def drive(self):
       
        print(f"The {self.color} {self.brand}")


print("Polymorphism Demonstration:")
garage = [
    Car("Toyota", "Red"),
    ElectricCar("Tesla", "Blue", battery_capacity_kwh=100),
    Truck("Ford", "Green", payload_capacity_kg=7500)
]
for vehicle in garage:
    vehicle.drive()
print("-" * 30)
print("\nBasic Car Object Usage:")
my_car = Car("Mercedes-Benz", "Silver")

print(f"My car is a {my_car.color} {my_car.brand}.")
my_car.drive()
print("-" * 30)