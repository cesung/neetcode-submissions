class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vis = set(nums)
        res = 0

        for num in nums:
            # to see if num is the start of the seq
            if num - 1 in vis:
                continue
            
            cnt = 0
            i = num
            while i in vis:
                cnt += 1 
                i += 1
            
            res = max(
                res,
                cnt
            )
            
        return res