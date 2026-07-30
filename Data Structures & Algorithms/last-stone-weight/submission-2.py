class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-1*stone for stone in stones]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) > 1:
            x = heapq.heappop(self.maxHeap)
            y = heapq.heappop(self.maxHeap)
            if y > x:
                heapq.heappush(self.maxHeap, x - y)
        heapq.heappush(self.maxHeap, 0)
        return abs(self.maxHeap[0])