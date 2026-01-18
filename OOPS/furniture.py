class Furniture:

    """Furniture Class"""
    def __init__(self, colour, material):
        self.colour = colour
        self.material = material

    def show_details(self):
        """fubction show details"""
        return (f"Furniture should be in {self.colour}"
                f"colour and should be made of {self.material}")


class Table(Furniture):

    """Table class"""
    def __init__(self, colour, material, height):
        super().__init__(colour, material)
        self.height = height

    def model(self):

        """Model function"""
        print("Table model 2215 is perfect for you")


t1 = Table("white", "wood", 10)
print(t1.show_details())