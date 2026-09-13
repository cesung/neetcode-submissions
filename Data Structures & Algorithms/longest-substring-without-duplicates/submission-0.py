class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        vis = set()
        right = 0

        max_size = 0

        for left in range(n):

            while right < n and s[right] not in vis:
                vis.add(s[right])
                right += 1
            
            max_size = max(
                max_size,
                right - left
            )
            vis.remove(s[left])

        return max_size
