# map function
# 1.
mylist = []
for x in range(1, 100):
    mylist.append(x)

new_list = map(lambda z: z+z, mylist)
print(list(new_list))


# 2.

my_map = map(lambda x1, x2: x1 % x2, (10, 11, 12), [1, 2, 3])
print(my_map)
# print result: <map object at ...>
# Map class is lazily evaluated.
# It means that
# I need to convert it into list/tuple/set.
print(list(my_map))
print(list(my_map))  # empty list :O
