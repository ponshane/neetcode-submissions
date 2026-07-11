class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = (x)**2 + (y)**2
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap)
        
        res = []
        while k > 0:
            d, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -=1
        
        return res