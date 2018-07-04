
twosomeArr = []
with open("2sum_data.txt") as f:
        for line in f:
                twosomeArr.append(int(line))
twosomeSet = set(twosomeArr)

twosomeCount = 0
for i in range(-10, 101):
        for el in twosomeArr:
                if (i - el) in twosomeSet:
                        print(i, el)
                        twosomeCount = twosomeCount + 1
                        break
print(twosomeCount)
