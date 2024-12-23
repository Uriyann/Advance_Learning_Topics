"""Sets = Collection which is unordered, unindexed, and no duplicate values."""

fruit = {"apple", "orange", "banana", "tea cup"}
dishes = {"bowl", "plate", "cup", "tea cup"}


fruit.add("pineapple")                # Adding a new variable
fruit.remove("orange")                # Removing a certain variable
fruit.clear()                         # Clearing the entier sets
fruit.update(dishes)                  # Updating the set and randomizing it

dinner_table = fruit.union(dishes)    # Updating the set and randomizing it
print(dinner_table)

for x in dinner_table:
    print(x, end= ", ")

print(dishes.difference(fruit))       # Printing the difference of dishes to fruits
print(fruit.intersection(dishes))     # Printing the similarity from fruits to dishes