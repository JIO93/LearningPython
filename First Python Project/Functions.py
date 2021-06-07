calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"

#A function is definited by using keyword def. Place your code in the indented section below the function name.
def days_to_units():
    print(f"20 days are {20 * calculation_to_seconds} {name_of_unit}")
    print("All Good!")

#Functions are only run when they are called as shown below. If you don't call the fuction nothing is displayed.
days_to_units()