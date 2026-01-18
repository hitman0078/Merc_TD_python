class BankAccount:
    """
    Represents a bank account with an account number, balance, and branch name.

    Attributes:
        account_number (str): A public identifier for the account.
        _branch_name (str): A protected attribute indicating the branch.
        __balance (float): A "private" attribute storing the account's balance.
    """

    def __init__(self, account_number: str, initial_balance: float = 0.0,
                 branch_name: str = "Main Branch") -> None:
        """
        Initializes a new BankAccount instance.
        """
        self.account_number = account_number
        self.__balance = initial_balance
        self._branch_name = branch_name

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self.__balance

    def set_balance(self, amount: float) -> None:
        """
        Sets the balance of the account to a new amount.

        Prevents setting a negative balance.

        Args:
            amount (float): The new balance amount to set.
        """
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")


if __name__ == "__main__":
    account = BankAccount("123456789", 1000.0)

    print(f"Account Number: {account.account_number}")

    print(f"Initial Balance: {account.get_balance()}")

    account.set_balance(1500.0)
    print(f"New Balance after set_balance(1500.0): {account.get_balance()}")

    account.set_balance(-200.0)
    print(f"Balance after set_balance(-200.0): {account.get_balance()}")