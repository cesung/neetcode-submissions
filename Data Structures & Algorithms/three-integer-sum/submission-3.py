class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            # [-3, -3, 1, 2]
            #       ^
            #       i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n -1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left + 1 < n and nums[left] == nums[left + 1]:
                        left += 1
                    while right - 1 >= 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur > 0:
                    right -= 1
                else:
                    left += 1
        
        return res
