class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        min_heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(min_heap)
        t = 0
        while min_heap:
            taken = []
            for _ in range(n + 1):
                if not min_heap:
                    break
                taken.append(heapq.heappop(min_heap) + 1)
            
            for c in taken:
                # if task still remain
                if c:
                    heapq.heappush(min_heap, c)
            
            t += (n+1) if min_heap else len(taken)
        
        return t