calculation_to_seconds = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    #A function can return data as a result. This is done by specifying return as shown below. 
    return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}"

#This will ask the user for input. Python stops executing when it comes to the input().
#The input function is provided by Python. We did not have to write it.
#\n makes it so the input is on a  new line. It is used for formatting and making the output in the terminal nicer. 
user_input = input("Enter a number of days and I will convert it to hours!\n")
#Below we are converting the user_input to an int instead of a string. This is called casting. This is a built in Python function.
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)