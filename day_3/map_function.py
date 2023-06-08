# map function
# syntax: map(function, iterable)
# 1.
mylist = []
for x in range(1, 100):
    mylist.append(x)

new_list = map(lambda z: z+z, mylist)
print(list(new_list))


# 2.

my_map = map(lambda x1, x2: x1 % x2, (10, 11, 12), [1, 2, 3])  # different data types and still works fine
print(my_map)
# print result: <map object at ...>
# Map class is lazily evaluated.
# It means that
# I need to convert it into list/tuple/set.
print(list(my_map))
print(tuple(my_map))  # empty tuple :O
#  Second print and map gets zeroed out
#  I guess that it is intended to be used once.
