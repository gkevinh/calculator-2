"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_entry = input("Please enter in your equation:  > ")
    user_entry.split(" ")
    num1 = user_entry[1]
    num2 = user_entry[2]
    num3 = user_entry[3]

    if user_entry == "q":
        print("EXIT")
        break

    else:
        if user_entry[0] == "square":
            square(num1)




# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)