class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for num in nums:
            
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                cur_min = minHeap[0]
                if num <= cur_min:
                    continue
                else:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, num)
        
        return minHeap[0]