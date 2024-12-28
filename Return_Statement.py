"""Return Statement = Functions send python values/object back to the caller.
                      These values/objects are known as the function's return value"""

def multiply(num1, num2):
    result = num1 * num2
    return result                   # The variable result will return back to the caller

multiply(6, 8)                      # Nothing will be printed as it returns back to the caller

print(multiply(6, 8))               # It will be printed as we used the print()
                                    # Output: 48

x = multiply(6, 8)                  # You can use variable as argument and it will return
print(x)                            # Output: 48

def multiply_ver2(num1, num2):
    return num1 * num2              # This would work as it was before but less lines

print(multiply_ver2(6, 6))          # Output: 36