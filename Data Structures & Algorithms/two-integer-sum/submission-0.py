class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vis = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in vis:
                return [vis[diff], idx]
            
            vis[num] = idx
        
        return [-1, -1]