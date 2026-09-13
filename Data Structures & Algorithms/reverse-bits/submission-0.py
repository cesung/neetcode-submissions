class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        i = 0
        while n:
            res |= (1 << (31-i)) if n % 2 else 0
            n >>= 1

            i += 1
        
        return res