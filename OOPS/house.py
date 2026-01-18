class House:
    """
    Represents a generic house with basic attributes and behaviors.
    """

    def __init__(self, address: str, num_rooms: int, area_sqm: int):
        """
        Initializes a new House object.

        :param address: The physical address of the house.
        :param num_rooms: The number of rooms in the house.
        :param area_sqm: The total area of the house in square meters.
        """
        self.address = address
        self.num_rooms = num_rooms
        self.area_sqm = area_sqm

    def display_info(self) -> None:
        """
        Prints basic information about the house.
        """
        print(f"Address: {self.address}")
        print(f"Rooms: {self.num_rooms}")
        print(f"Area: {self.area_sqm} sqm")

    def describe_location(self) -> None:
        """
        Describes the general location of the house.
        """
        print(f"This house is located at {self.address}.")


class Apartment(House):
    """
    Represents an apartment, inheriting from House, with additional attributes.
    """

    def __init__(self, address: str,
                 num_rooms: int,
                 area_sqm: int,
                 floor_number: int):
        """
        Initializes a new Apartment object.

        :param address: The physical address of the apartment.
        :param num_rooms: The number of rooms in the apartment.
        :param area_sqm: The total area of the apartment in square meters.
        :param floor_number: The floor number where the apartment is located.
        """
        super().__init__(address, num_rooms, area_sqm)
        self.floor_number = floor_number

    def display_info(self) -> None:
        """
        Overriding the base method.
        """
        super().display_info()
        print(f"Floor: {self.floor_number}")

    def describe_location(self) -> None:
        """
        Describes the specific location of the apartment.
        """
        print(f"At: {self.floor_number} at {self.address}.")


class DetachedHouse(House):
    """
    Represents a detached house.
    """

    def __init__(self, address: str,
                 num_rooms: int,
                 area_sqm: int,
                 has_garden: bool):
        """
        Initializes a new DetachedHouse object.

        :param address: The physical address of the detached house.
        :param num_rooms: The number of rooms in the detached house.
        :param area_sqm: The total area of the detached house in square meters.
        :param has_garden: Boolean indicating if the house has a garden.
        """
        super().__init__(address, num_rooms, area_sqm)
        self.has_garden = has_garden

    def display_info(self) -> None:
        """
        Prints detailed information about the detached house.
        """
        super().display_info()  # Call base class method for common info
        print(f"Has Garden: {'Yes' if self.has_garden else 'No'}")

    def describe_location(self) -> None:
        """
        Describes the specific location of the detached house.
        """
        garden_status = "with garden" if self.has_garden else "without garden"
        print(f"At: {garden_status} is located at {self.address}.")


print("Polymorphism Demonstration (display_info):")
properties = [
    House("123 Main St", 4, 150),
    Apartment("456 Oak Ave, Apt 3B", 2, 80, 3),
    DetachedHouse("789 Pine Ln", 5, 200, True)
]

for prop in properties:
    print("\n--- Property Details ---")
    prop.display_info()

print("\n" + "-" * 30 + "\n")

print("Polymorphism Demonstration (describe_location):")
for prop in properties:
    prop.describe_location()

print("\n" + "-" * 30 + "\n")

print("Basic House Object Usage:")
my_house = House("101 Elm St", 3, 120)

print(f"My house at {my_house.address} has {my_house.num_rooms} rooms.")
my_house.display_info()