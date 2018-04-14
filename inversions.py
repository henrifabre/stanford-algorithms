def get_inversions2(array):
        inv_list = []
        for i in range(len(array)):
                for elem in array[i+1:]:
                        if array[i] > elem:
                                inv_list.append([array[i], elem])
        return inv_list


# In: unsorted array
# Out1: count of inversions
# Out2: sorted array
def get_inversions(array):
        mid = int(len(array)/2)
        if mid == 0:
                return 0, array
        lo_count, lo_list = get_inversions(array[:mid])
        hi_count, hi_list = get_inversions(array[mid:])
        split_count, sorted_list = merge_count(lo_list, hi_list)
        return lo_count+hi_count+split_count, sorted_list


# In: two SORTED arrays
# In3: count of split inversions so far
# Out1: count of split inversions
# Out2: One merged sorted array
def merge_count(lo_list, hi_list):
        out_list = []
        split_count = 0
        if len(lo_list) == 0:
                return 0, hi_list
        elif len(hi_list) == 0:
                return 0, lo_list
        else:
                while len(hi_list) > 0 and len(lo_list) > 0:
                        if lo_list[0] <= hi_list[0]:
                                out_list.append(lo_list.pop(0))
                        else:
                                out_list.append(hi_list.pop(0))
                                split_count += len(lo_list)
        out_list.extend(lo_list)
        out_list.extend(hi_list)
        return split_count, out_list
