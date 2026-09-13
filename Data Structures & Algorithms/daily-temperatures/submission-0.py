class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [-1 for _ in range(n)]
        # (idx, temp)
        stk = []

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][1]:
                res[stk[-1][0]] = i - stk[-1][0]
                stk.pop()
            
            stk.append( (i, t) )
        
        while stk:
            idx, _ = stk.pop()
            res[idx] = 0
        
        return res
            
