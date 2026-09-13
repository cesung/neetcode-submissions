class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            return sum(math.ceil(p / k) for p in piles) <= h

        left, right = 1, 10**15
        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid
        
        return left