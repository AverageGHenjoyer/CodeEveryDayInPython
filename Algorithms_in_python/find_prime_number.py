# 13.06.2023
# Test if given number is a prime number
user_input = 0
while user_input < 2:
    try:
        user_input = int(input("Enter a number, so I will check if it is a prime number \n"))
    except ValueError:
        print("Invalid input. Sorry for inconvenience. Please try again.")


for x in range(2, user_input):
    if user_input % x == 0:
        print("It is not a prime number... :/")
        break
    else:
        print("It is a prime number! :O")
        break
