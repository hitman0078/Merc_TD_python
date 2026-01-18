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

from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from types import MappingProxyType
from typing import Iterable, FrozenSet, List, Tuple, Union

# --- 1) Fixed offerings (immutable) ---
BASIC_FLAVORS: Tuple[str, ...] = ("Vanilla", "Chocolate", "Strawberry")  # cannot be changed


# --- 2) Pricing lookup (read-only view for safety) ---
# Internal mutable dict (not exposed); you could load this from config if needed.
__prices = {
    "Vanilla": 2.50,
    "Chocolate": 3.00,
    "Strawberry": 3.25,
}
PRICES = MappingProxyType(__prices)  # external code cannot mutate this


# --- 3) Strict serving rules (immutable Enum) ---
class Serving(Enum):
    CONE = "Cone"
    CUP = "Cup"


# --- 4) Order record (frozen so it can't be altered after creation) ---
@dataclass(frozen=True)
class Order:
    flavor: str
    serving: Serving
    toppings: FrozenSet[str]   # unique & order-agnostic
    price: float               # price for the flavor
    timestamp: datetime


class IceCreamShop:
    """Core shop logic: lookups, validation, and transaction tracking."""

    def __init__(self) -> None:
        self._history: List[Order] = []  # running list of successful sales

    # Fast price lookup with validation
    def get_price(self, flavor: str) -> float:
        if flavor not in BASIC_FLAVORS:
            raise ValueError("Unknown flavor; menu is fixed to signature offerings.")
        return PRICES[flavor]

    # Place an order and record it in history
    def place_order(
        self,
        flavor: str,
        serving: Union[Serving, str],
        toppings: Iterable[str] = (),
    ) -> Order:
        # Validate flavor against immutable menu
        if flavor not in BASIC_FLAVORS:
            raise ValueError("Unknown flavor; menu is fixed to signature offerings.")

        # Normalize/validate serving (only Cone or Cup allowed)
        if isinstance(serving, str):
            try:
                serving_enum = Serving(serving.title())  # accepts "cone", "CONE", etc.
            except ValueError:
                raise ValueError('Serving must be either "Cone" or "Cup".')
        else:
            serving_enum = serving

        # Unique, order-agnostic toppings (cleanup whitespace, ignore empties)
        toppings_set: FrozenSet[str] = frozenset(
            t.strip().lower() for t in toppings if t and t.strip()
        )

        price = PRICES[flavor]
        order = Order(
            flavor=flavor,
            serving=serving_enum,
            toppings=toppings_set,
            price=price,
            timestamp=datetime.now(),
        )
        self._history.append(order)  # track successful sale
        return order

    # Immutable snapshot so callers can’t mutate internal history
    def order_history(self) -> Tuple[Order, ...]:
        return tuple(self._history)


# --- Example usage / quick test ---
if __name__ == "__main__":
    shop = IceCreamShop()

    print("Menu (immutable):", BASIC_FLAVORS)
    print("Price lookup (Chocolate):", shop.get_price("Chocolate"))

    # Place a couple of orders
    o1 = shop.place_order("Vanilla", "cone", ["Nuts", "sprinkles", "nuts"])  # duplicates removed
    o2 = shop.place_order("Strawberry", Serving.CUP, {"Cherry"})             # set input also works

    # Review history at closing
    for i, o in enumerate(shop.order_history(), start=1):
        print(
            f"#{i} | {o.timestamp:%H:%M:%S} | {o.flavor} ({o.serving.value}) "
            f"| toppings={sorted(o.toppings)} | total=${o.price:.2f}"
        )