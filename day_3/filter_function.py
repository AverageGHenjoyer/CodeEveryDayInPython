# Filter function syntax:
# filter(function, iterable)
import random

# 1.


def is_even(number):
    if number % 2 == 0:
        return True
    return False


my_list = []
for num in range(100, 1000):
    my_list.append(num)

even_numbers_list = list(filter(is_even, my_list))
print(even_numbers_list)


# 2. Combining filter() func with a map() function
def add_random_number(number):
    return number + random.randint(1,1000)


def is_three_digit(digit):
    if digit >= 100:
        return True
    return False


my_final_list = list(map(add_random_number, filter(is_three_digit, even_numbers_list)))
print(my_final_list)

