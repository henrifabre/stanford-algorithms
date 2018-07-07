import line_profiler


twosomeSet = set()
with open("2sum_data.txt") as f:
        for line in f:
                twosomeSet.add(int(line))
print(len(twosomeSet))


# @profile
def twosome_count(twosomeSet):
        twosomeCount = 0
        for i in range(-10000, 10001):
                for el in twosomeSet:
                        if (i - el) in twosomeSet:
                                print(i, el)
                                twosomeCount = twosomeCount + 1
                                break
        print(twosomeCount)


twosome_count(twosomeSet)
