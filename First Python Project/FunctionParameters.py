calculation_to_seconds = 24
name_of_unit = "hours"

#A parameter is information that can be passed into functions. Parameters are also called arguments
#The parameters are num_of_days and custom_message. Putting it inside the brackets allows us to enter any number/text we like when we call the fucntion.
#You can setup as many parameters as you'd like. Here we only setup two.
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}")
    print("All Good!")

#The parameter value is not hard coded as we have to type it in everytime we call the funcation as shown below.
days_to_units(20, "Awesome!")
days_to_units(35, "Looks Good!")
