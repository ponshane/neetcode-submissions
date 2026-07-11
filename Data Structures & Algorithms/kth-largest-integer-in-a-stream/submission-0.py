class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k
        # in-place operation
        heapq.heapify(nums)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
