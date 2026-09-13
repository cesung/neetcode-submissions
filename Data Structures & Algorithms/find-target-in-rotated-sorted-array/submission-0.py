class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        def bs(left, right):
            while left < right:
                mid = (left + right) // 2 + 1
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            
            return -1 if nums[left] != target else left
        
        is_rotated = nums[0] > nums[-1]
        n = len(nums)
        if not is_rotated:
            return bs(0, n - 1)
        
        # find the rotation point: first element in the array is < than nums[0]
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid
        
        rotation_point = left
        return bs(0, rotation_point - 1) if target >= nums[0] else bs(rotation_point, n - 1)

        