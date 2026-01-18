# You have been hired to build a management system for a new boutique
# ice cream shop, "Scoops & Scripts." The shop owner needs a robust program
# that ensures the menu remains permanent, prices are easily searchable, and
# order history is tracked accurately.

# Project Requirements
# Your task is to implement a system using Python that handles different types of
# data with specific constraints:

# Fixed Offerings: The basic flavors (Vanilla, Chocolate, Strawberry)
# are the shop's signature and should never be accidentally changed or
# deleted during the program's execution.

# Pricing Lookup: Each flavor has a specific price. The system must
# quickly find the cost of a flavor to calculate a customer's bill.

# Strict Serving Rules: To prevent inventory errors, the shop only
# allows two types of serving: Cone or Cup. This rule is set in stone and must
# be immutable.

# Customization: Customers can choose multiple toppings. These toppings
# should be unique (you can't have "nuts" twice), and the order doesn't matter.

# Transaction Tracking: The system must maintain a running history of
# every successful sale made throughout the day so that the manager can
# review them at closing.



import datetime


FLAVORS = frozenset(["Vanilla", "Chocolate", "Strawberry"])

PRICES = {
    "Vanilla": 300,
    "Chocolate": 350,
    "Strawberry": 325,
    "Sprinkles": 50,
    "Hot Fudge": 100,
    "Whipped Cream": 75,
    "Cherries": 60,
    "Nuts": 75,
    "Gummy Bears": 80
}

SERVING_TYPES = frozenset(["Cone", "Cup"])

AVAILABLE_TOPPINGS = frozenset([
    "Sprinkles", "Hot Fudge", "Whipped Cream", "Cherries", "Nuts",
    "Gummy Bears"
])

TRANSACTION_HISTORY = []


def display_menu():
    """
    Displays the available ice cream flavors and their prices.
    """
    print("\nFlavors:")
    for flavor in sorted(list(FLAVORS)):
        print(f"- {flavor}: INR {PRICES.get(flavor, 'N/A'):.2f}")


def display_serving_options():
    """
    Displays the available serving options.
    """
    print("\nServing Options:")
    for serving in sorted(list(SERVING_TYPES)):
        print(f"- {serving}")


def display_available_toppings():
    """
    Displays the available toppings and their prices.
    """
    print("\nAvailable Toppings:")
    for topping in sorted(list(AVAILABLE_TOPPINGS)):
        price = PRICES.get(topping, 0.00)
        print(f"- {topping}: INR {price:.2f}")


def place_order(flavor: str, serving_type: str, chosen_toppings: list = None):
    """
    Processes a customer's order, calculates the total, and records the
    transaction.

    Args:
        flavor (str): The chosen ice cream flavor.
        serving_type (str): The chosen serving type ("Cone" or "Cup").
        chosen_toppings (list, optional): A list of toppings selected by the
                                          customer. Defaults to None.

    Returns:
        dict or None: The recorded transaction details if successful,
                      otherwise None.
    """
    if flavor not in FLAVORS:
        print(f"Error: '{flavor}' is not a valid flavor.")
        return None

    if serving_type not in SERVING_TYPES:
        print(f"Error: '{serving_type}' is not a valid serving type. "
              "Please choose 'Cone' or 'Cup'.")
        return None

    total_price = PRICES[flavor]

    customer_toppings = set(chosen_toppings) if chosen_toppings else set()

    valid_customer_toppings = set()
    invalid_toppings = []
    for topping in customer_toppings:
        if topping not in AVAILABLE_TOPPINGS:
            invalid_toppings.append(topping)
        else:
            valid_customer_toppings.add(topping)
            total_price += PRICES.get(topping, 0.00)

    if invalid_toppings:
        print(f"Warning: The following toppings are not available and were "
              f"ignored: {', '.join(invalid_toppings)}")

    transaction = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "flavor": flavor,
        "serving_type": serving_type,
        # Store as sorted list for consistent representation
        "toppings": sorted(list(valid_customer_toppings)),
        "total_price": total_price
    }
    TRANSACTION_HISTORY.append(transaction)
    print(f"\nOrder placed successfully! Total: INR {total_price:.2f}")
    return transaction


def get_transaction_history():
    """
    Returns the complete history of all sales made.

    Returns:
        list: A list of dictionaries, each representing a recorded transaction.
    """
    return TRANSACTION_HISTORY


def review_daily_sales():
    """
    Prints a summary of all transactions for the day.
    """
    if not TRANSACTION_HISTORY:
        print("\nNo sales recorded today yet.")
        return

    print("\nDaily Sales Review:")
    grand_total = 0.0
    for i, transaction in enumerate(TRANSACTION_HISTORY):
        toppings_str = ", ".join(transaction["toppings"]) \
            if transaction["toppings"] else "None"
        print(f"Sale {i+1} ({transaction['timestamp']}):")
        print(f"  Flavor: {transaction['flavor']}")
        print(f"  Serving: {transaction['serving_type']}")
        print(f"  Toppings: {toppings_str}")
        print(f"  Total: INR {transaction['total_price']:.2f}")
        grand_total += transaction['total_price']
        print("-" * 20)
    print(f"Grand Total for the Day: INR {grand_total:.2f}")


if __name__ == "__main__":
    display_menu()
    display_serving_options()
    display_available_toppings()

    place_order("Vanilla", "Cup", ["Sprinkles", "Hot Fudge"])
    place_order("Chocolate", "Cone", ["Nuts", "Sprinkles", "Nuts"])
    place_order("Strawberry", "Cup")
    place_order("Vanilla", "Cone",
                ["Whipped Cream", "Cherries", "NonExistentTopping"])
    place_order("Mint Chip", "Cup")
    place_order("Vanilla", "Bowl")

    review_daily_sales()