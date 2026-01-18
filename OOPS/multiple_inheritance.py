# Parent class 1
class Calling:

    """Calling class"""
    def feature1(self):

        """Feature 1"""
        print("Calling feature")


# Parent class 2
class Camera:

    """Camera class"""
    def feature2(self):

        """Feature 2"""
        print("Camera feature")


# Child class (Multiple Inheritance)
class SmartPhone(Calling, Camera):
    """Smartphone class"""
    def explore(self):

        """Explore"""
        print("Exploring features of SmartPhone")


phone = SmartPhone()
phone.feature1()
phone.explore()