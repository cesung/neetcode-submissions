class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0
        for num in nums:
            val ^= num
        
        for i in range(len(nums) + 1):
            val ^= i
        
        return val