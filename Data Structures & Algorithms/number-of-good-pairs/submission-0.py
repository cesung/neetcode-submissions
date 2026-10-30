class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        res = 0
        for k,v in cntr.items():
            res += v*(v-1)//2
        
        return res