class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cntr = Counter(s)
        t_cntr = Counter(t)
        return s_cntr == t_cntr