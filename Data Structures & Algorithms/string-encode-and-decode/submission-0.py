class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            encoding += str(len(s)) + "," + s
        
        return encoding

    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0
        while i < n:
            j = i
            while s[j] != ',':
                j += 1
            l = int(s[i:j])
            res.append(s[j+1:j+1+l])
            i = j+1+l
    
        return res


