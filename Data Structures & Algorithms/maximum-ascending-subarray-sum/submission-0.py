class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n, maxs, curs = len(nums), nums[0], nums[0]
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                maxs = max(
                    maxs,
                    curs
                )
                curs = nums[i]
            else:
                curs += nums[i]

        maxs = max(
            maxs,
            curs
        )
        
        return maxs
