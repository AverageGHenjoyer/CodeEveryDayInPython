user_input = int(input("Give me a number: \n"))


def calc_the_factorial(x):
    if x == 0:
        return 1
    else:
        return x*calc_the_factorial(x-1)


print(f"Calculated factorial: {calc_the_factorial(user_input)}")
