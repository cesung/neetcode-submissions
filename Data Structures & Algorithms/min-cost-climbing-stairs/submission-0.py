class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        min_cost = [0 for _ in range(size + 1)]
        for i in range(2, size + 1):
            min_cost[i] = min(
                min_cost[i - 1] + cost[i - 1],
                min_cost[i - 2] + cost[i - 2],
            )
        
        return min_cost[-1]