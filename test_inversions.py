import inversions


# arr = [6, 5, 3, 4, 2, 1]
arr = []

# ## Following code is for reading specific number of lines
# with open("h1_IntegerArray.txt") as f:
#         for i in range(50000):
#
with open("h1_IntegerArray.txt") as f:
        for line in f:
                arr.append(int(line))

# ## Method for getting inversions in quadratic time
# inversions2 = inversions.get_inversions2(arr)
# print(len(inversions2))

count, sorted_list = inversions.get_inversions(arr)

print(count)
# print(sorted_list)
