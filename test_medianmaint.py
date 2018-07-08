from medianmaint import MinHeap, MaxHeap


minHeap = MaxHeap()
maxHeap = MinHeap()
medianEl = None
medianSum = 0
# Invariant: len(minHeap) <= len(maxHeap)
# Invariant: len(maxHeap) - len(minHeap) <= 1
with open("Median.txt") as f:
        for line in f:
                newEl = int(line)
                if medianEl is None:
                        medianEl = newEl
                        # print(minHeap.heap, " >>", medianEl, "<< ", maxHeap.heap)
                        medianSum += medianEl
                        continue
                if maxHeap.len() == 0:
                        if newEl < medianEl:
                                maxHeap.push(medianEl)
                                medianEl = newEl
                        else:
                                maxHeap.push(newEl)

                        # print(minHeap.heap, " >>", medianEl, "<< ", maxHeap.heap)
                        medianSum += medianEl
                        continue
                if minHeap.len() == 0:
                        if newEl < medianEl:
                                minHeap.push(newEl)
                        else:
                                minHeap.push(medianEl)
                                medianEl = maxHeap.pop()
                                if newEl < medianEl:
                                        maxHeap.push(medianEl)
                                        medianEl = newEl
                                else:
                                        maxHeap.push(newEl)
                        # print(minHeap.heap, " >>", medianEl, "<< ", maxHeap.heap)
                        medianSum += medianEl
                        continue
                if minHeap.len() == (maxHeap.len() - 1):
                        if newEl < medianEl:
                                minHeap.push(newEl)
                        else:
                                minHeap.push(medianEl)
                                medianEl = maxHeap.pop()
                                if newEl < medianEl:
                                        maxHeap.push(medianEl)
                                        medianEl = newEl
                                else:
                                        maxHeap.push(newEl)
                        # print(minHeap.heap, " >>", medianEl, "<< ", maxHeap.heap)
                        medianSum += medianEl
                elif minHeap.len() == maxHeap.len():
                        if newEl < medianEl:
                                maxHeap.push(medianEl)
                                medianEl = minHeap.pop()
                                if newEl < medianEl:
                                        minHeap.push(newEl)
                                else:
                                        minHeap.push(medianEl)
                                        medianEl = newEl
                        else:
                                maxHeap.push(newEl)
                        # print(minHeap.heap, " >>", medianEl, "<< ", maxHeap.heap)
                        medianSum += medianEl
                else:
                        print("Error!!")
                        break
print(medianSum)
