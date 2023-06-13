# Sieve of Eratosthenes
while True:
    try:
        given_number = int(input("Please enter a number: \n"))
    except ValueError:
        print("An error occurred. Please try again.")
    else:
        break

my_list = list(range(3, given_number))

for y in my_list[:]:
    if y > 2 and y % 2 == 0:

        my_list.remove(y)

for z in my_list[:]:
    if z > 3 and z % 3 == 0:
        my_list.remove(z)

for e in my_list[:]:
    if e > 5 and e % 5 == 0:
        my_list.remove(e)

print(f"Prime number list from a given number is as follows: {my_list}")