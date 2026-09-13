class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k

        def quickSelect(l, r):
            pivot, ptr = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[r], nums[ptr] = nums[ptr], nums[r]
        
            if ptr > k:
                return quickSelect(l, ptr - 1)
            elif ptr < k:
                return quickSelect(ptr + 1, r)
            
            return nums[ptr]
        
        return quickSelect(0, n - 1)
