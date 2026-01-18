class Car:

    """Car function"""
    def __init__(self, brand):
        self.brand = brand

    def drive(self):

        """Default behavior for a standard car"""
        print(f"{self.brand}: Vroom vroom! (Engine roaring)")


class ElectricCar(Car):

    """Electric car class"""
    def drive(self):
        """ Overriding the parent behavior with something specific"""
        print(f"{self.brand}: ... (Silent electric hum)")


class Truck(Car):

    """Truck class"""
    def drive(self):
        """Another variation"""
        print(f"{self.brand}: Rumble rumble! (Heavy diesel engine)")


# --- Proving Polymorphism ---

# We create a list containing different types of vehicles
garage = [Car("Toyota"), ElectricCar("Tesla"), Truck("Ford")]

for vehicle in garage:
    # We call the EXACT same method name on every object
    # Python automatically picks the "right" version for each object
    vehicle.drive()