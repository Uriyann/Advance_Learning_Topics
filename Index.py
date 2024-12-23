"""Index Operator [] = Gives access to a sequence's element
                       (str, list, tuples)"""

name = "joshie Borrow!"

# if(name[0].islower()):            # It will determine if the variable is in lowercase letters
#     name = name.capitalize()      # It will then capitalize the lowercase letters

# first_name = name[0:6].upper()    # It will make the variable 'name' uppercase
first_name = name[:6].upper()       # You dont need 0 to make it work as it is automatically starts from 0
last_name = name[7:].lower()        # It will make the last name a lowercase letters
last_char = name[-1]

print(first_name)                   # Output: JOSHIE
print(last_name)                    # Output: borrow!
print(last_char)                    # Output: !