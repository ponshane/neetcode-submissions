class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = Counter(tasks)
        maxHeap = [-cnt for cnt in cnts.values()]
        heapq.heapify(maxHeap)

        q = deque() # [n, waiting time]
        time = 0
        
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                # if n is not zero
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
