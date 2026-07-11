class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones] # turn to maxHeap
        # inplace operation
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = -1 * maxHeap[0]
            heapq.heappop(maxHeap)
            x = -1 * maxHeap[0]
            heapq.heappop(maxHeap)

            if x < y:
                new_y = y - x
                heapq.heappush(maxHeap, -1 * new_y)
        
        return -1 * maxHeap[0] if len(maxHeap) > 0 else 0