#A variable is only available from inside the region it is created.
#Global Scope = Variables available from within any scope
#Local Scope = Variables created inside a function

calculation_to_seconds = 24
name_of_unit = "hours"

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}")
    print("All Good!")

def scope_check():
    #Global scope because it is accessible in this function.
    print(name_of_unit)
    #Local scope because it is erroring out when trying to call it in this function.
    #If you want this code to run enter num_of_days inside the parenthesis of the scope_check() function.
    print(num_of_days)
    #Internal variable because it is defined inside of a function. This variable cannot be called by another fucntion unless you specify it in that function as well.
    my_var = "Variable Inside Function"
    print(my_var)

scope_check(20)