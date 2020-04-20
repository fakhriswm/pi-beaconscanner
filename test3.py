l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del l[0]
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

del l[-1]
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8]

del l[6]
print(l)
# [1, 2, 3, 4, 5, 6, 8]
