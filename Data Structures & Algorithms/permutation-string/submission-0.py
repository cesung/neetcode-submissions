class Solution:
    def check_permutation(self, s1_cntr, s2_cntr):
        for i in range(26):
            if s1_cntr[i] != s2_cntr[i]:
                return False
        
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        s1_cntr, s2_cntr = [0 for _ in range(26)], [0 for _ in range(26)]
        for ch in s1:
            s1_cntr[ord(ch) - ord('a')] += 1

        right = 0

        for left in range(n2):
            while right < n2 and (right - left) < n1:
                s2_cntr[ord(s2[right]) - ord('a')] += 1
                right += 1
            
            if self.check_permutation(s1_cntr, s2_cntr):
                return True
            
            s2_cntr[ord(s2[left]) - ord('a')] -= 1
        
        return False
