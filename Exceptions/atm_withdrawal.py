class ATM:
    
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def withdraw_money(self, amount):
        """
        :raises ValueError: If the amount is not greater than zero.
        :raises RuntimeError: If there is insufficient balance.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if amount > self.balance:
            raise RuntimeError("Insufficient BALANCE")

        self.balance -= amount
        return self.balance

    def deposit_money(self, amount):
        """
        :raises ValueError: If the amount is not greater than zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount
        return self.balance

atm_machine = ATM(5000)

try:
    print("Welcome to the ATM")
    user_input = input("Enter amount to withdraw: ")
    withdrawal_amount = float(user_input)

    remaining_balance = atm_machine.withdraw_money(withdrawal_amount)
    print("Withdrawal successful!")
    print(f"Remaining BALANCE: ₹{remaining_balance}")
except ValueError as ve:
    print("Input Error:", ve)
except RuntimeError as re:
    print("Transaction Error:", re)
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
else:
    print("Transaction completed without errors.")
finally:
    print("\n--- SESSION CLOSED ---")
    print("Thank you for using the ATM!")