class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def bs(d):
            l, r = 0, n -1
            while l < r:
                m = (l + r) // 2
                if days[m] <= d:
                    l = m + 1
                else:
                    r = m
            
            return l

        n = len(days)
        spent = [0 for _ in range(n + 1)]

        for i, day in enumerate(days):
            spent[i + 1] = min(
                spent[i] + costs[0],
                spent[bs(day - 7)] + costs[1],
                spent[bs(day - 30)] + costs[2]
            )
        
        return spent[-1]