class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            if x == y:
                continue
            
            new_stone = abs(x - y)
            heapq.heappush(stones, -1 * new_stone)
        
        return -1 * stones[0] if stones else 0