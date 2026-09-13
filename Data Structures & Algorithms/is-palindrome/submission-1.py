class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        left, right = 0, n - 1
        while left < right:
            while left < n and s[left].isalnum() == False:
                left += 1
            while right >= 0 and s[right].isalnum() == False:
                right -= 1

            if left > right:
                break
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True