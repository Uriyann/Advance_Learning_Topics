"""Dictionary = A changeable, unordered collection of unique key: 
                value pairs. They are fast because they use hashing,
                allowing us to access a value quickly"""

capitals = {
    "USA":"Washington DC",
    "India":"New Dehli",
    "China":"Beijing",
    "Russia":"Moscow"
}

print(capitals["USA"])                # Washington DC
print(capitals["Germany"])            # Error
print(capitals.get("Germany"))        # None
print(capitals.keys())                # dict_keys(['USA', 'India', 'China', 'Russia'])
print(capitals.values())              # dict_values(['Washington DC', 'New Dehli', 'Beijing', 'Moscow'])
print(capitals.items())               # dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])

capitals.update({"Germany":"Berlin"}) # Added Germany to the dictionary
print(capitals["Germany"])            # Berlin
capitals.update({"USA":"Las Vegas"})  # Changed the capital of USA
print(capitals["USA"])                # Las Vegas
capitals.pop("China")                 # Removes China from keys and its values

print(capitals.popitem())             # Printing the last key and value

for key,value in capitals.items():    
    print(key,value)                  # USA Las Vegas
                                      # India New Dehli
                                      # Russia Moscow
                                      # Germany Berlin