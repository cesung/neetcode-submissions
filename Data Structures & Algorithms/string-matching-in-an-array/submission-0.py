class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def rolling_hash(pattern, text):
            BASE, MOD = 31, 1_000_000_007
            n, m = len(pattern), len(text)

            MSB = pow(BASE, n-1, MOD)
            pat_hash = 0
            for i in range(n):
                pat_hash = (pat_hash * BASE + ord(pattern[i])) % MOD

            win_hash = 0
            for i in range(n):
                win_hash = (win_hash * BASE + ord(text[i])) % MOD
            
            for i in range(m - n + 1):
                if (
                    pat_hash == win_hash and
                    pattern == text[i:i+n]
                ):
                    return True
                
                if i + n < m:
                    win_hash = ((win_hash - ord(text[i])*MSB) * BASE + ord(text[i+n])) % MOD
            
            return False

        words.sort(key=lambda x : len(x))
        res, n = [], len(words)

        for i in range(n):
            for j in range(i+1, n):
                if rolling_hash(words[i], words[j]):
                    res.append(words[i])
                    break
        
        return res