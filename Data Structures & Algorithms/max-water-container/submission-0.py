class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        max_area = 0

        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            max_area = max(
                max_area,
                h * w
            )

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_area