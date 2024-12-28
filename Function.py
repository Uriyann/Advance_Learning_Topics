"""Function = a block of code which is executed only when it is called."""

def hello(name):
    print("hello! " + name)
    print("have a nice day\n")

hello("Luck")                                       # Will execute the function hello() once
hello("Amy")                                        # Output: hello! Amy
                                                    # have a nice day

my_name = "Uriii"                                   # Variables can be used as arguments
hello(my_name)                                      # Output: hello! Uriii
                                                    # have a nice day

def hellow(first_name, last_name, age):             # You can add more arguments in a single function
    print("hallo! "+first_name+" "+last_name)
    print("you are",age,"years old")                # You can have integer as an argument  
    print("have a nice day")

hellow("Noel", "Stollen", 18)                       # Output: hallo! Noel Stollen
                                                    #         you are 18 years old
                                                    #         have a nice day