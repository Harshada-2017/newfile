# Create a custom exception named InsufficientBalanceError:

# Set balance = 10000.
# Accept a withdrawal amount.
# Raise your custom exception if withdrawal exceeds the balance.
# Otherwise deduct the amount and print the remaining balance.
# Handle your custom exception with except.

class InsufficientBalanceError(Exception):
    pass

balance = 10000
withdrwal=int(input("Enter a amount to withdraw:"))
try:
    if withdrwal>balance:
        raise InsufficientBalanceError("withdrawal exceeds the balance.")
    remaining_balance=balance-withdrwal
    print("remaining balance:",remaining_balance)
    
except InsufficientBalanceError as e:
    print(e)
    