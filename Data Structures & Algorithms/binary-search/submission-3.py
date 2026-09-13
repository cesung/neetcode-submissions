class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        
        if nums[l] == target:
            return l
        
        return -1