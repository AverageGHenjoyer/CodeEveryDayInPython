#
# def calc_the_factorial(x:int) -> int:
#     if x == 0:
#         return 1
#     else:
#         return x*calc_the_factorial(x-1)
#
#
# while True:
#     try:
#         user_input = int(input("Give me a number: \n"))
#     except ValueError:
#         print("Something has gone wrong. Please try again.")
#     else:
#         print(f"Calculated factorial: {calc_the_factorial(user_input)}")
#         break

# 2.
def factorial(x, tmp=1):
    if x == 0:
        return tmp
    else:
        return factorial(x-1, tmp*x)


while True:
    try:
        given_number = int(input("Give me a number: \n"))
    except ValueError:
        print("Something has gone wrong. Please try again.")
    else:
        print(f"Calculated factorial: {factorial(given_number)}")
        break
