# Accept a number from the user.
# Convert it to an integer.
# Divide 100 by the number.
# Handle invalid input using ValueError.
# Handle division by zero using ZeroDivisionError.
# Print Calculation completed using finally.

a=int(input("enter a number:"))
try:
    c=100/a
except ValueError:
    print("invalid input using ValueError")
except ZeroDivisionError:
    print("division by zero using ZeroDivisionError")
finally:
    print("Calculation completed using finally")
    
