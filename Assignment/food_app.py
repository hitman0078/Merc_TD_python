class Food:
    def __init__(self, food_id, name, category, price):
        self.food_id = food_id
        self.name = name
        self.category = category
        self.price = price
 
    def display(self):
        print(f"{self.food_id}. {self.name} ({self.category}) --> Rs.{self.price}")

class Menu:
    def __init__(self, outlet_name, outlet_id):
        self.outlet_name = outlet_name
        self.outlet_id = outlet_id
        self.food_items = []

    def show_menu(self):
        print(f"\n|||| Menu | {self.outlet_name} (Outlet ID: {self.outlet_id}) ||||\n")
        for food in self.food_items:
            food.display()


    def add_food(self, food):
        self.food_items.append(food)

 
    def get_food_by_id(self, food_id):
        for food in self.food_items:
            if food.food_id == food_id:
                return food
        return None
    
class Cart:
    def __init__(self):
        self.items= {}

    def add_to_cart(self, food, quantity):
        if food in self.items:
            self.items[food] += quantity
        else:
            self.items[food] = quantity
    
    def show_cart(self):
        print("\n||| Your Cart |||")
        if not self.items:
            print("No items in cart.")
            return
        
        total = 0
        gtotal = 0

        for food, qty in self.items.items():
            cost = food.price * qty
            total += cost 
            gtotal == total * 1.18
        
            print(f"{food.name} x {qty} = ₹{cost}")
 
        print(f"TOTAL CART VALUE: ₹{total}")

    def calculate_total(self):
        return sum(food.price * qty for food, qty in self.items.items())        
    

class FoodApp:
    def __init__(self):
        self.menu = Menu("Pizza Hut", 623)
        self.cart = Cart()
        self.load_menu()
 
    def load_menu(self):
        self.menu.add_food(Food(1, "Farmhouse Pizza", "Pizza", 399))
        self.menu.add_food(Food(2, "Salami Pizza", "Pizza", 299))
        self.menu.add_food(Food(3, "Veg Exotica", "Pizza", 249))
        self.menu.add_food(Food(4, "Cheese Pizza", "Pizza", 399))
        self.menu.add_food(Food(5, "BBQ Pizza", "Pizza", 269))
        self.menu.add_food(Food(6, "Garlic Bread", "Sides", 149))
        self.menu.add_food(Food(7, "Parcel Veg", "Sides", 160))
        self.menu.add_food(Food(8, "Sprite", "Beverage", 60))
        self.menu.add_food(Food(9, "Miranda", "Beverage", 60))
        self.menu.add_food(Food(10, "Coke", "Beverage", 60))
        self.menu.add_food(Food(11, "Lemon Soda", "Beverage", 60))
        self.menu.add_food(Food(12, "Chipotle Dip", "Add-On", 10))

    def start(self):
        while True:
            print("\n1. Today's Menu")
            print("2. Add Item to Cart")
            print("3. View Cart")
            print("4. Place Order")
            print("5. Exit")
 
            choice = input("Enter task choice: ")
 
            if choice == "1":
                self.menu.show_menu()
 
            elif choice == "2":
                self.menu.show_menu()
                food_id = int(input("Provide Food ID: "))
                qty = int(input("Enter Quantity: "))
                food = self.menu.get_food_by_id(food_id)

                if food:
                    self.cart.add_to_cart(food, qty)
                    print("Item added to cart.")
                else:
                    print("INVALID Food ID.")
 
            elif choice == "3":
                self.cart.show_cart()
 
            elif choice == "4":
                gtotal = self.cart.calculate_total()
                if gtotal == 0:
                    print("Cart is empty.")
                else:
                    print("\nOrder Placed Successfully!")
                    print(f"Final Amount: Rs.{gtotal}")
                    break
 
            elif choice == "5":
                print("Thank you for visiting Pizza Hut!")
                break
 
            else:
                print("Invalid choice. Try again.")
 
 
app = FoodApp()
app.start()


        


