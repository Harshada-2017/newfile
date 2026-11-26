# Write a driving-license eligibility program:

# Accept the user's age.
# If age is less than 18, raise a ValueError.
# Handle the exception and print an appropriate message.
# Otherwise, display Eligible for driving license

age=int(input("enter a age:"))
try:
    if age<18:
        raise ValueError("age is less than 18")
except ValueError as e:
    print(e)
else:
    print("Eligible")