class InsufficientBalanceError(Exception):
    pass



balance = 5000
withdrawal = 4000

try:
    if withdrawal > balance:
        raise InsufficientBalanceError("Insufficient bank balance")

    balance = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
    print("Transaction failed:", e)

finally:
    print("Thank you for using our bank")