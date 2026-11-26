# result = 10 / 0

# try:
#     print(result)
# except ZeroDivisionError:
#     print("Error")
    
# try:
#     print("A")
#     x = 10 / 0
#     print("B")
# except ZeroDivisionError:
#     print("C")
# print("D")

#Output=A
#C
#D

# try:
#     x = int("50")
#     print(x)
# except ValueError:
#     print("Error")
# else:
#     print("Success")
# finally:
#     print("End")
    
# try:
#     x = int("abc")
#     print("A")
# except ValueError:
#     print("B")
# else:
#     print("C")
# finally:
#     print("D")
    
# try:
#     print(10 / 2)
# except ZeroDivisionError:
#     print("Error")
# finally:
#     print("Done")

try:
    x = 10
    y = 0
    print(x / y)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zero Division")
else:
    print("Success")
finally:
    print("Finished")