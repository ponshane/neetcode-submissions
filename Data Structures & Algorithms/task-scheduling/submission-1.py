class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = Counter(tasks)
        maxHeap = [-cnt for cnt in cnts.values()]
        heapq.heapify(maxHeap)

        q = deque() # [cnt, waiting time]
        time = 0
        
        while maxHeap or q:
            time += 1

            if maxHeap:
                # simulate cpu processing
                cnt = 1 + heapq.heappop(maxHeap) 
                # if n is non-zero, it means we need to process it after n cycles
                if cnt:
                    q.append((cnt, time + n))
            
            # when it is the time to release the task (FIFO)
            if q and q[0][1] == time:
                # push back the cnt back to maxHeap
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
