

# In 1: array to be partitioned
# In 2: Left index of subarray (0 based count)
# In 3: Right index of subarray (exclusive)
def partitionArr(arr, l_index, r_index, pivot_index):
        # Choose pivot element (here it is first element)
        pivot = arr[pivot_index]
        arr[pivot_index] = arr[l_index]
        arr[l_index] = pivot
        pivot_index = l_index
        for j in range(l_index + 1, r_index):
                if arr[j] < pivot:
                        temp = arr[pivot_index+1]
                        arr[pivot_index+1] = arr[j]
                        arr[j] = temp
                        pivot_index += 1
        arr[l_index] = arr[pivot_index]
        arr[pivot_index] = pivot
        return pivot_index


# Just starting out
def quicksort(arr):
        cmp_count = 0
        if len(arr) <= 1:
                return arr, 0
        else:
                el_first = arr[0]
                el_last = arr[-1]
                idx_mid = int((len(arr)+1)/2) - 1
                el_mid = arr[idx_mid]
                tmp_list = [el_first, el_mid, el_last]
                tmp_list.sort()
                if tmp_list[1] == el_first:
                        split_index = partitionArr(arr, 0, len(arr), 0)
                elif tmp_list[1] == el_mid:
                        split_index = partitionArr(arr, 0, len(arr), idx_mid)
                else:
                        split_index = partitionArr(arr, 0, len(arr), -1)
                cmp_count = len(arr)-1
                [arr[:split_index], ucnt] = quicksort(arr[:split_index])
                [arr[split_index+1:], lcnt] = quicksort(arr[split_index+1:])
                cmp_count += ucnt + lcnt
                return arr, cmp_count
