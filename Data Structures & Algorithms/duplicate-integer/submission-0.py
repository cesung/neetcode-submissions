class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vis = set()

        for num in nums:
            if num in vis:
                return True
            vis.add(num)
        
        return False