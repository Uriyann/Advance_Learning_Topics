"""Nested Function Calls = Are functions that we define inside other functions to directly access the variables and names defined in the enclosing function."""

num = input("Enter a positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)                                                              # This way of method can have too many lines and it can be confusing

print(round(abs(float(input("Enter another positive number: ")))))      # Efficient and less lines of code when nested