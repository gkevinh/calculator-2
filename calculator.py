"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


while True:
    user_entry = input("Please enter in your equation:  > ")
    tokens = user_entry.split(" ")
    result = None
    operator = tokens[0]

    if "q" in tokens:
        print("EXIT")
        break

    num1 = tokens[1]

    if len(tokens) < 2:
        print("Not enought numbers.")
        continue

    if len(tokens) < 3:
        num2 = "0"

    else:
        num2 = tokens[2]

    result = None

    if len(tokens) > 3:
        num3 = tokens[3]


    elif operator == "+":
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

