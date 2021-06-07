#Below you see us defining the variables. There are reserved words in Python that you can't use as a variable. You can look these up online. 
#Make sure you use descriptive variable names. This way anyone who uses your code can easily see what your variables do.
calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"

#Below you see how to insert the variables into the code. Python recognizes they are variables because they are inside of {}.
print(f"20 days are {20 * calculation_to_seconds} {name_of_unit}")
print(f"20 days are {35 * calculation_to_seconds} {name_of_unit}")
print(f"20 days are {50 * calculation_to_seconds} {name_of_unit}")
print(f"20 days are {110 * calculation_to_seconds} {name_of_unit}")