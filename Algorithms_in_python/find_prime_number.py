# 13.06.2023
# Test if given number is a prime number
while True:
    try:
        user_input = int(input("Enter a number, so I will check if it is a prime number \n"))
    except ValueError:
        print("Invalid input. Sorry for inconvenience. Please try again.")
    else:
        break
if user_input < 2:
    print("Invalid number. Please try again.")
elif user_input > 1:
    for x in range(2, user_input):
        if (user_input % x) == 0:
            print(f"{user_input} is not a prime number... :/")
            print(f"Found divider: {x}")
            break
    else:
        print("It is a prime number! :O")


else:
    print(user_input,"is not a prime number")