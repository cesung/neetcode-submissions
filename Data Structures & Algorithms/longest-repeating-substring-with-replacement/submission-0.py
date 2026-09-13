class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def _is_valid(right):
            return (
                (right - left + 1) -
                max(
                    max(freq),
                    freq[ord(s[right]) - ord('A')] + 1
                )
            ) <= k

        n = len(s)
        freq = [0 for _ in range(26)]
        res = 1

        right = 0
        for left in range(n):
            while (
                right < n and
                _is_valid(right)
            ):
                freq[ord(s[right]) - ord('A')] += 1
                right += 1
            
            res = max(
                res,
                right - left
            )
            freq[ord(s[left]) - ord('A')] -= 1
        
        return res

            
