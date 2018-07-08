import heapq


class MinHeap:
        heap = []

        def len(self):
                return len(self.heap)

        def pop(self):
                return heapq.heappop(self.heap)

        def push(self, el):
                heapq.heappush(self.heap, el)


class MaxHeap:
        heap = []

        def len(self):
                return len(self.heap)

        def pop(self):
                return -heapq.heappop(self.heap)

        def push(self, el):
                heapq.heappush(self.heap, -el)
