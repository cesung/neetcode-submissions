class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nxt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[nxt - 1]:
                nums[i], nums[nxt] = nums[nxt], nums[i]
                nxt += 1
        
        return nxt