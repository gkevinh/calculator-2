"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)
""" imports arithmetic module with the add, subtract, multiply, divide, square, cube, power, and mod funtions"""

while True:  #create a while loop and loops until you enter q for quit
    user_entry = input("Please enter in your equation:  > ")   #ask user to enter in equation
    tokens = user_entry.split(" ")   #use split function to put each entry into a list
    result = None   #create a place to store the return value
    operator = tokens[0]   #create variable 

    if "q" in tokens:   #enter in q to exit the calculator
        print("EXIT")
        break

    if len(tokens) < 2:   #if user enters in one charater, prints not enough entered
        print("Not enought numbers.")
        continue

    num1 = tokens[1]   #create variable num1 to be the first number you enter

    if len(tokens) < 3:   #if user enters in two entries num2 is set to a string of zero
        num2 = "0"

    else:
        num2 = tokens[2]   

    if not num1.isdigit() or not num2.isdigit():   #check to make sure num1 and num2 are digits
        print("Please enter numbers.")
        continue


    if operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))

    print(result)

