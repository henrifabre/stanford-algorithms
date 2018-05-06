import quicksort as qs


# arr = [6, 5, 3, 4, 2, 1]

arr = []

# ## Following code is for reading specific number of lines
# with open("h1_IntegerArray.txt") as f:
#         for i in range(50000):
#
with open("QuickSort.txt") as f:
        for line in f:
                arr.append(int(line))

# ## Method for getting inversions in quadratic time
# inversions2 = inversions.get_inversions2(arr)
# print(len(inversions2))

sorted_list, count = qs.quicksort(arr)

print(sorted_list)
print(count)
