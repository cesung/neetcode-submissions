class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        def check(v):
            if v == 1:
                return True

            if v in vis:
                return False

            vis.add(v)

            t = 0
            while v:
                t += (v % 10)**2
                v //= 10
            
            return check(t)
        
        return check(n)

        