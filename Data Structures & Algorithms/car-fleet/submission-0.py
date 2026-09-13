class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [
            (p, s)
            for p, s in zip(position, speed)
        ]

        pairs.sort(key = lambda x: x[0])
        n = len(pairs)
    
        stk = [ (target - pairs[-1][0]) / pairs[-1][1] ]
        for i in range(n - 1, -1, -1):
            p, s = pairs[i]
            t = (target - p) / s
            if t > stk[-1]:
                stk.append(t)

        return len(stk)