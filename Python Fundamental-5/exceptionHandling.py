"""
using try, except, else, finally
"""
try:
    x = int(input("Enter a number : "))
    ans = 10/x
except ZeroDivisionError:
    print("Divide by zero is not allowed")
except (ValueError):
    print("Invalid input")
else:
    print(f"ans = {ans}")
finally:
    print("Finally")