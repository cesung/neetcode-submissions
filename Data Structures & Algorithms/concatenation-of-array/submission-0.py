class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ret = [0 for _ in range(size * 2)]

        for i in range(size):
            ret[i] = ret[i + size] = nums[i]
        
        return ret